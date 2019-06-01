# -*- coding: utf-8 -*-
import scrapy,re,json
from ..items import SzseprojectItem

class SzseSpider(scrapy.Spider):
    name = 'szse'
    allowed_domains = ['www.szse.cn']
    start_urls = ['http://www.szse.cn/']

    def start_requests(self):
        # 原始页拿不到数据，改访问数据接口url
        # start_url = 'http://www.szse.cn/market/stock/list/index.html'
        for page in range(1,109):
            start_url = 'http://www.szse.cn/api/report/ShowReport/data?SHOWTYPE=JSON&CATALOGID=1110&TABKEY=tab1&PAGENO={}'.format(page)
            yield scrapy.Request(url=start_url,callback=self.parse_info)

    def parse_info(self, response):
        # 获取数据，解析json，正则or字典取值匹配提取目标字段
        datajson = json.loads(response.text)[0]
        # 目标数据json
        data = datajson['data']
        for jsondata in data:
            item = SzseprojectItem()
            # 下面链接href为股票代码详情页的url，但是直接访问该接口并不能获取数据，数据是通过其他接口传入的
            # href = re.findall("href='(.*?)' target=",jsondata['gsjc'])[0]
            gsjcdata = re.findall('<u>(.*?)</u>',jsondata['gsjc'])[0]
            item['gsjc'] = gsjcdata
            zqdm = jsondata['zqdm']
            item['zqdm'] = zqdm
            item['agdm'] = jsondata['agdm']
            item['agjc'] = jsondata['agjc']
            item['agssrq'] = jsondata['agssrq']
            item['agzgb'] = jsondata['agzgb']
            item['agltgb'] = jsondata['agltgb']
            item['sshymc'] = jsondata['sshymc']
            # 进入股票代码代码详情页接口：http://www.szse.cn/api/report/index/companyGeneralization?random=0.7857520210454887&secCode=000001
            zqdmhref = 'http://www.szse.cn/api/report/index/companyGeneralization?secCode={}'
            next_url = zqdmhref.format(zqdm)
            yield scrapy.Request(url=next_url,callback=self.parse_page,meta={'item':item})

    def parse_page(self,response):
        item = response.meta['item']
        detailsjson = json.loads(response.text)
        detailsdata = detailsjson['data']
        item['gsqc'] = detailsdata['gsqc']
        item['ywqc'] = detailsdata['ywqc']
        item['zcdz'] = detailsdata['zcdz']
        item['bgdm'] = detailsdata['bgdm']
        item['bgjc'] = detailsdata['bgjc']
        item['bgssrq'] = detailsdata['bgssrq']
        item['bgzgb'] = detailsdata['bgzgb']
        item['bgltgb'] = detailsdata['bgltgb']
        item['dldq'] = detailsdata['dldq']
        item['sheng'] = detailsdata['sheng']
        item['shi'] = detailsdata['shi']
        item['http'] = detailsdata['http']
        yield item
