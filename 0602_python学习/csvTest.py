#文件读写操作
import csv

file = open('G:/fan/2020学期/2020春/大数据实训/编程及学习/jobs.csv','w',encoding='utf-8')

'''
#当作最基本的文件进行处理
for line in file.readlines():
    print(line)
'''

#将file声明，绑定为csv文件
write = csv.writer(file)
#可以通过csv文件对象进行读写操作
write.writerow(
    str(
        '这是我新写的,我现在好想听歌……atfirst……title,job_company,salary,address,experience'
        .split(',')
    )
)
#这个会把原来的给搞没了不知道为什么

file.close()
