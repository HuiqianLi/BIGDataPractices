# Spark RDD 练习作业：
# 选择部分数据（可以是自拟，可以是采集的，也可以是现有的），
# 进行多角度数据统计及分析，并进行数据整合及展示
# （尽量多的运用 Spark RDD API）

# 说明：csv文件为scrapy爬虫作业爬取的游戏列表🙃
# 每一列分别为英文名、中文名、发行日期、评分、游戏原网站、价格、steam购买/下载链接
# English_name 、Chinese_name、release_date、score、website、price、download_link

from pyspark import SparkContext,SparkConf

# 构建 配置对象
conf = SparkConf().setAppName('SparkRDDtest').setMaster('local[*]')

# 构建 环境对象
sc = SparkContext(conf=conf)

originRDD = sc.textFile('games.csv')

# 将游戏英文名写入English_name.txt文件
file_handle=open('English_name.txt',mode='a+',encoding='utf-8')

# print(originRDD.count())
# print(originRDD.take(2))
for item in originRDD.collect():
    file_handle.write(item[:item.index(',')] + '\n')

file_handle.close()