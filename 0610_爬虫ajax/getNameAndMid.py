import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import read_csv
# h2 data-v-0fd2c70d="" class="name txt-inline"

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/67.0.3396.79 Safari/537.36'
    }

# 去掉<><>标签
def noh2(exmlist):
    exmlist = exmlist[47:-5]
    return exmlist

# 去掉前后缀
# //space.bilibili.com/17409016?from=search
def nopre(exmlist):
    exmlist = exmlist[21:-12]
    return exmlist

name_list = []
mid_list = []

# 获取百大UP用户名
path = "name.html"
htmlfile = open(path, 'r', encoding='utf-8')
htmlhandle = htmlfile.read()

soup = BeautifulSoup(htmlhandle,  'lxml')
origin_name_list = soup.find_all('h2', class_="name txt-inline")
for item in origin_name_list:
    # print(noh2(str(item)))
    username = noh2(str(item))
    name_list.append(username)

    # 根据用户名搜索mid
    # 筛选条件：UP、粉丝由高到低第一个
    url = 'https://search.bilibili.com/upuser?keyword={}&page=1&user_type=1&order=fans&order_sort=0'\
        .format(username)
    response = requests.get(url, headers)
    response.encoding = response.apparent_encoding
    # print(response.text)

    # <div class="headline"><!----><a href="//space.bilibili.com/162367996?from=search" title="爱做芋头的饭SAMA" target="_blank"
    # class="title">爱做芋头的饭SAMA</a>
    soup = BeautifulSoup(response.text,  'lxml')
    up_url = soup.find('div', class_="headline").find('a')['href']
    userid = nopre(up_url)
    mid_list.append(userid)
    # print(nopre(up_url))

print(mid_list)
dataframe = pd.DataFrame({'name':name_list,'mid':mid_list})
dataframe.to_csv("名单.csv", index=False, sep=',', encoding='utf-8')