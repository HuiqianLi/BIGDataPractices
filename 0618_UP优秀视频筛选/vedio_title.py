import csv
import json
import pandas as pd

# UPlist = ['爱做饭的芋头SAMA']
UPlist = []
avidList = []

file_in = 'unConvertResults.json'
originFile = open(file_in,'r',encoding='utf-8')


dataset = json.load(originFile)
for i in range(len(dataset)):
    UPlist.append(dataset[i]['up_name'])

for item in UPlist:
    file_path = 'G:/fan/2020学期/2020春/大数据实训/0615_商业价值计算/data/' + item + '.csv'
    file_out = 'title/'+ item +'.txt'
    file_handle = open(file_out,mode='w',encoding='utf-8')
    with open(file_path,'r',encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        # rows = [row for row in reader]
        for row in reader:                  #跳过第一行
            break
        for row in reader:
            title = row[0]            #标题
            file_handle.write(title)

file_handle.close()