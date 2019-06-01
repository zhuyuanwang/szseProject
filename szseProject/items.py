# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SzseprojectItem(scrapy.Item):
    ## 目标字段如下
    # 公司代码
    zqdm = scrapy.Field()
    # 公司简称
    gsjc = scrapy.Field()
    # A股代码
    agdm = scrapy.Field()
    # A股简称
    agjc = scrapy.Field()
    # A股上市日期
    agssrq = scrapy.Field()
    # A股总股本（亿股）
    agzgb = scrapy.Field()
    # A股流通股本（亿股）
    agltgb = scrapy.Field()
    # 所属行业
    sshymc = scrapy.Field()
    ##进入详情页后添加的字段
    # 公司全称
    gsqc = scrapy.Field()
    # 英文全称
    ywqc = scrapy.Field()
    # 注册地址
    zcdz = scrapy.Field()
    # B股代码
    bgdm = scrapy.Field()
    # B股简称
    bgjc = scrapy.Field()
    # B股上市日期
    bgssrq = scrapy.Field()
    # B股总股本
    bgzgb = scrapy.Field()
    # B股流通股本
    bgltgb = scrapy.Field()
    # 地区
    dldq = scrapy.Field()
    # 省份
    sheng = scrapy.Field()
    # 城市
    shi = scrapy.Field()
    # 公司网址
    http = scrapy.Field()
