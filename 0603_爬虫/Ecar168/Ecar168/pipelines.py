# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv, pandas


# 将Ecar168 采集到的数据，存储到 csv 中
class Ecar168Pipeline(object):

    # 对象初始化函数
    def __init__(self):
        self.file = open('ecar168.csv', 'a+', encoding='utf-8', newline='')
        self.writer = csv.writer(self.file)

    # 对 spider 传递过来的 item 对象进行处理
    def process_item(self, item, spider):
        # 数据处理：比如缺失数据整理、删除；重复数据清理；不合理数据的整理

        # 数据存储
        self.writer.writerow(
            [item['year'], item['month'], item['category'], item['sub_category'], item['ranking'], item['manufacturer'],
             item['vehicle_type'], item['sales']])

        return item

    def close_spider(self, spider):
        self.file.close()

        # df = pandas.read_csv('ecar168.csv', delimiter=',',
        #                      names=['year', 'month', 'category', 'sub_category', 'ranking', 'manufacturer',
        #                             'vehicle_type',
        #                             'sales'])
        # df = df.sort_values(['year', 'month'],axis=1)
        # df.to_csv('ecar168_sorted.csv')
