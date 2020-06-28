# 作业04
# 使用 Spark SQL 技术对 20190315.csv 航班数据
# 进行规整及统计分析（从个人认为合理的角度进行分析），
# 航班的数据列意义分别是：
# 起始地，目的地，航班日期，xx（此列忽略），航空公司，航班，出发时间，到达时间，准点率，最低价
# starting,destination,date,xx,company,flight,start_time,arrive_time,punctuality_rate,minprice 
# 注意：做好注释
from pyspark.sql import Row
from pyspark.sql import SparkSession

session = SparkSession \
    .builder \
    .appName("test") \
    .master('local[*]')\
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# 读取CVS格式的数据，转换为DataFrame
df = session.read.csv('20190315.csv')
# 结构化展示数据
df.show()

