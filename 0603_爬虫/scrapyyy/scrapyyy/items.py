# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyyyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    English_name = scrapy.Field()   #英文名
    Chinese_name = scrapy.Field()   #中文名
    release_date = scrapy.Field()   #发行日期
    score = scrapy.Field()          #评分
    website = scrapy.Field()        #游戏原网站
    price = scrapy.Field()          #价格
    # introduction = scrapy.Field() #游戏简介
    # 网站上有的有简介，有的没有简介，没有的返回None后面会出错_(:з)∠)_……就直接删掉了
    download_link = scrapy.Field()  #steam购买/下载链接

    pass
