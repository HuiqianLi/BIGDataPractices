# -*- coding: utf-8 -*-
# Scrapy 练习作业：
# 选择一个感兴趣的方向或者课题相关的方向的网站数据进行采集，
# 数据不限定与API接口、网页、JS注入内容，
# 并将数据保存csv或MySQL或Redis；
# 有兴趣的同学可以试试 Scrapy 和 Redis 连用的分布式爬虫

# 作业描述：
# 爬取INDIA NOVA网站中的 https://indienova.com/
# --必买 STEAM 独立游戏--页面中 https://indienova.com/steam/mustbuy/p/5
# 榜单及所含游戏详细信息
import scrapy
from bs4 import BeautifulSoup

from scrapyyy.items import ScrapyyyItem

class GamesSpider(scrapy.Spider):
    name = 'games'
    allowed_domains = ['indienova.com']
    prefix = 'https://indienova.com'
    start_urls = ['https://indienova.com/steam/mustbuy']

# 第一步：取到必买游戏的所有分页链接
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')  # xpath

        # 对每一分页链接发起请求
        for i in range(1, 5):
            url = 'https://indienova.com/steam/mustbuy/p/{}'.format(i)
            yield scrapy.Request(url=url, callback=self.parse_link)
    
    # 采集必买游戏入口页面链接，并发起详情请求
    def parse_link(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        divs = soup.find_all('div', class_="steam-game")

        for div in divs:
            # 获取链接
            # print("title=",'{}{}'.format(self.prefix, div.find('a')['href']))
            yield scrapy.Request(url='{}{}'.format(self.prefix, div.find('a')['href']), callback=self.parse_detail)

    # 采集游戏详情
    def parse_detail(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        # To the Moon :: 去月球
        title = soup.find('section', id="page-title").find('div',class_="container clearfix").find('h1').string
        steam_infos = soup.find('ul',class_="list-group steam-info").find_all('li',class_="list-group-item")

        item = ScrapyyyItem()
        item['English_name'] = str(title)[:str(title).index('::')].strip()
        item['Chinese_name'] = str(title)[str(title).index('::') + 2:].strip()
        item['release_date'] = str(steam_infos[1])[-15:-5].strip()
        item['score'] = steam_infos[2].find('a').string
        item['website'] = steam_infos[3].find('a')['href']
        item['price'] = str(steam_infos[4])[str(steam_infos[4]).index('</strong>') + 9:str(steam_infos[4]).index('（<a')].strip()
        # item['introduction'] = soup.find('div',class_="indie-intro").find('p').string
        item['download_link'] = soup.find('iframe')['src']
        
        # print(item)
        # item['introduction'] = str(introduc).strip()

        yield item