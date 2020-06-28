# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Ecar168Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    year = scrapy.Field()
    month = scrapy.Field()
    # 大类
    category = scrapy.Field()
    # 小类
    sub_category = scrapy.Field()
    # 排名
    ranking = scrapy.Field()
    # 厂商
    manufacturer = scrapy.Field()
    # 车型
    vehicle_type = scrapy.Field()
    # 销量
    sales = scrapy.Field()
