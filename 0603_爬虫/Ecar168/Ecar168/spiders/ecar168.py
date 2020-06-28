# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

from Ecar168.items import Ecar168Item


class Ecar168Spider(scrapy.Spider):
    name = 'ecar168'
    allowed_domains = ['ecar168.cn']
    prefix = 'http://www.ecar168.cn'
    # scrapy 框架默认的起始请求设定
    start_urls = ['http://www.ecar168.cn/xiaoliang/liebiao/2_0.htm']

    # 也可以自己去定义起始的逻辑
    # def start_requests(self):
    #     for i in range(52):
    #         url = 'http://www.ecar168.cn/xiaoliang/liebiao/1_{}.htm'.format(i * 30)
    #         yield scrapy.Request(url=url, callback=self.parse)

    # 第一步：取到 SUV 销量排行的所有分页链接
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')  # xpath
        span = soup.find('span', class_="hong")

        # 对每一分页链接发起请求
        for i in range(0, int(span.string)):
            url = 'http://www.ecar168.cn/xiaoliang/liebiao/2_{}.htm'.format(i * 30)
            yield scrapy.Request(url=url, callback=self.parse_link)

    # 采集排行榜入口页面链接，并发起详情请求
    def parse_link(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        uls = soup.find_all('ul', class_="biaoti_ul")

        for ul in uls:
            yield scrapy.Request(url='{}{}'.format(self.prefix, ul.find('a')['href']), callback=self.parse_detail)

    # 采集销量详情
    def parse_detail(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        title = soup.find('div', class_="biaoti").find('h1').string
        # 2018年3月自主紧凑型SUV销量排行榜
        print('title:', title)

        year = str(title)[:str(title).index('年')].strip()
        month = str(title)[str(title).index('年') + 1:str(title).index('月')].strip()
        category = str(title)[str(title).index('型') + 1:str(title).index('销量')].strip()
        sub_category = str(title)[str(title).index('月') + 1:str(title).index('型') + 1].strip()

        trs = soup.find_all('tr', class_="yuefen_tr")
        for tr in trs:
            tds = tr.find_all('td')

            item = Ecar168Item()
            item['year'] = year
            item['month'] = month
            item['category'] = category
            item['sub_category'] = sub_category

            item['ranking'] = tds[0].string.strip()
            item['manufacturer'] = tds[1].string.strip()

            if tds[2].find('a'):
                item['vehicle_type'] = tds[2].find('a').string.strip()
            else:
                item['vehicle_type'] = tds[2].string.strip()

            item['sales'] = tds[3].string.strip()

            # print(item)

            # 数据处理，在这？不；将数据回传，进入 Pipeline 中进行处理
            yield item
