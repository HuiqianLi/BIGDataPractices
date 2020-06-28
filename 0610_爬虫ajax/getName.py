# h2 data-v-0fd2c70d="" class="name txt-inline"
# https://www.bilibili.com/blackboard/activity-BPU2019.html?spm_id_from=333.788.b_636f6d6d656e74.11#/stage3
from bs4 import BeautifulSoup
import pandas as pd

#去掉<><>标签
def noh2(exmlist): 
    exmlist = exmlist[47:-5]
    return exmlist

path = "name.html"
htmlfile = open(path, 'r', encoding='utf-8')
htmlhandle = htmlfile.read()
name_list = []
soup = BeautifulSoup(htmlhandle,  'lxml')
origin_name_list = soup.find_all('h2',class_="name txt-inline")
for item in origin_name_list:
    print(noh2(str(item)))
    name_list.append(noh2(str(item)))
# print(type(name_list))
# print(name_list)
dataframe = pd.DataFrame({'name':name_list})
dataframe.to_csv("名单.csv", index=False, sep=',', encoding='utf_8_sig')

