# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# up：头像，简介，粉丝数，点赞总数，播放总数，发布视频数量（关注数）

import scrapy


class ScrapyyyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mid = scrapy.Field()        #用户ID
    name = scrapy.Field()       #用户名
    sex = scrapy.Field()        #性别
    face = scrapy.Field()       #头像
    # sign = scrapy.Field()       #签名
    follower = scrapy.Field() #关注列表
    fans = scrapy.Field()       #粉丝
    

    pass
