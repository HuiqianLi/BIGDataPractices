from pyspark import SparkContext,SparkConf

# 构建 配置对象
conf = SparkConf().setAppName('PriceOver50').setMaster('local[*]')

# 构建 环境对象
sc = SparkContext(conf=conf)

# 说明：csv文件为scrapy爬虫作业爬取的游戏列表🙃
# 每一列分别为英文名、中文名、发行日期、评分、游戏原网站、价格、steam购买/下载链接
# English_name 、Chinese_name、release_date、score、website、price、download_link

originRDD = sc.textFile('games.csv')

# 异常数据：第15行： "Papers, Please",入境管理处,
# 爬虫的时候用\t分吧，不知道怎么判断它是否异常……，改成"Papers Please"了
    
def handle(line):
    x = line.split(",")
    return x[1], x[5]
    # return x[1], int(x[3])

# 将输出结果写入result.txt文件
file_handle=open('result.txt',mode='a+',encoding='utf-8')
file_handle.write('3.计算价格高于50的：\n')

# 计算价格高于50的
MapRDD = originRDD.map(lambda line: handle(line))

filterRDD = MapRDD.filter(lambda x: int(str(x[1])[1:]) >= 50)#.map(lambda x: x[0])

for item in filterRDD.collect():
    file_handle.write(str(item) + '\n')

file_handle.write('-------------------------------------\n')

file_handle.close()