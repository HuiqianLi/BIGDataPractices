from pyspark import SparkContext,SparkConf

# 构建 配置对象
conf = SparkConf().setAppName('MapRDD').setMaster('local[*]')

# 构建 环境对象
sc = SparkContext(conf=conf)

originRDD = sc.textFile('English_name.txt')

# 将输出结果写入result.txt文件
file_handle=open('result.txt',mode='a+',encoding='utf-8')
file_handle.write('1.统计游戏名中出现的英文单词数量：\n')

# 统计游戏名中出现的英文单词频率
flatMapRDD = originRDD.flatMap(lambda row: str(row).replace('\n', ' ').split(' '))

mapRDD = flatMapRDD.map(lambda word: (word, 1))

reduceByKeyRDD = mapRDD.reduceByKey(lambda a, b: a + b)
# 按照键排序
sortByKeyRdd = reduceByKeyRDD.sortByKey()
for item in sortByKeyRdd.collect():
    file_handle.write(str(item) + '\n')

file_handle.write('-------------------------------------\n')

file_handle.close()