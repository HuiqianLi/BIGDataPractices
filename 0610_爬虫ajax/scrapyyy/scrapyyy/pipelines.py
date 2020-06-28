# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv, pandas

class ScrapyyyPipeline:

    # 对象初始化函数
    def __init__(self):
        self.file = open('test.csv', 'a+', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)

    # 对 spider 传递过来的 item 对象进行处理
    def process_item(self, item, spider):
        # 数据处理：比如缺失数据整理、删除；重复数据清理；不合理数据的整理

        # 数据存储
        self.writer.writerow(
            [\
                item['mid'],item['name'],item['sex'],item['face'],item['fans'],item['follower']\
            ])
        return item


def close_spider(self, spider):
        self.file.close()