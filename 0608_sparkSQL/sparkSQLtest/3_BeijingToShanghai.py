from pyspark.sql import Row
from pyspark.sql import SparkSession

# 筛选北京到上海的所有航班
# 将运行结果写入result.txt文件
file_handle=open('result.txt',mode='a+',encoding='utf-8')
file_handle.write('3.筛选北京到上海的所有航班:\n')

session = SparkSession \
    .builder \
    .appName("3_BeijingToShanghai") \
    .master('local[*]')\
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

sc = session.sparkContext
# 将数据源转换为RDD
originRDD = sc.textFile('20190315.csv')

# 将RDD内容转换为Row类型的键值对数据类型
rowRDD = originRDD.map(lambda x:str(x).split(','))\
    .map(lambda p:Row(\
    starting=p[0],\
    destination=p[1],\
    date=p[2],\
    company=p[4],\
    flight=p[5],\
    start_time=p[6],\
    arrive_time=p[7],\
    punctuality_rate=p[8],\
    minprice=p[9]))
# 以RDD为数据源，构建DataFrame
df = session.createDataFrame(rowRDD)
# df.show()

df.createOrReplaceTempView('airplanes')

# 北京到上海的所有航班
df1 = session.sql('select * from airplanes where starting = "北京" and destination = "上海" ')

# 以DataFrame为数据源，构建RDD，并将原始Row类型数据内容转换为基本数据列
transferRDD = df1.rdd.map(lambda row:(\
    'starting:' + row.starting, \
    'destination:' + row.destination,\
    'company:'+row.company,\
    'flight:'+row.flight))
# print(transferRDD.collect())

# 太多了😭，只取二十个
# for item in transferRDD.collect():
for item in transferRDD.take(20):
    file_handle.write(item.__str__() + '\n')

file_handle.write('-------------------------------------------------------------------\n')

file_handle.close()