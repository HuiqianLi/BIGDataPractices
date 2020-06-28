# -*- coding: utf-8 -*-
# 视频：播放，弹幕，收藏，评论，投币，转发，时长，发布时间，分区，tag
# up：头像，简介，粉丝数，点赞总数，播放总数，发布视频数量（关注数）

import scrapy
from bs4 import BeautifulSoup

from scrapyyy.items import ScrapyyyItem
from urllib.parse import urlencode
import json

class GamesSpider(scrapy.Spider):
    name = 'games'
    allowed_domains = ['api.bilibili.com']
    prefix = 'https://api.bilibili.com/x/web-interface/card?'
    # start_urls = ['https://space.bilibili.com/35091622']

    def start_requests(self):
        mids = [35091622]
        # mid = 35091622
        for mid in mids:
            start_url = self.prefix + urlencode({'mid': mid})
            # start_url = '{}{}'.format(self.prefix, mid)
            yield scrapy.Request(url=start_url, callback=self.parse_json, dont_filter=True)
        return super().start_requests()

    def parse_json(self,response):
        try:
            data = json.loads(response.body)
        except Exception:
            # 如果json文件解析失败，重新爬取该页面
            return scrapy.Request(url=response.url, callback=self.parse_json)
        code = int(data['code'])
        if code != 0:
            # code不为0则表示结果异常
            return scrapy.Request(url=response.url, callback=self.parse_json)
        card = data['data']['card']
        item = ScrapyyyItem()
        item['mid'] = card['mid']        #用户ID
        item['name'] = card['name']       #用户名
        item['sex'] = card['sex']        #性别
        item['face'] = card['face']       #头像
        # sign = scrapy.Field()       #签名
        item['fans'] =  card['fans']      #粉丝
        item['follower'] = data['data']['follower']
        yield item