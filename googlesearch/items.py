# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class GooglesearchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 关键词
    keywords = scrapy.Field()

    # 域名
    domain = scrapy.Field()

    # 排名
    rank = scrapy.Field()

    # 创建时间
    created_at = scrapy.Field()

    # 更新时间
    updated_at = scrapy.Field()
    pass
