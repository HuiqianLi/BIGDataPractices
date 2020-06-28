# Requests数据采集练习作业：
# 使用 Requests 和 Beautiful Soup 采集归档
# https://www.xicidaili.com ;
# 网站上的所有代理地址（Schema://IP:Port）
# 注意验证代理地址的有效性；
# 归档可选 csv 文件或 MySQL 数据库
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

headers = {
    'Connection':'keep-alive',
    #模拟浏览器操作
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def getHTMLText(url):
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

# # 构建解析对象，参数1：源数据HTML网页源代码;参数2：解析模式
# soup = BeautifulSoup(html,'lxml')

import bs4
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('table', {'id': 'ip_list'}).children:
        if isinstance(tr, bs4.element.Tag):     #如果tr标签不是bs4库定义的Tag类型将过滤掉
            tds = tr('td')                      #将所有的td标签存为一个列表类型tds
            for i in tds:
                i = str(i)
                #print(i)
                #print('------------------------------------')
                ulist.append(i)
            #ulist.append([tds[0].string])
    #print(ulist)
    return ulist

#去掉<td></td>
def nottd(exmlist): 
    for i in range(len(exmlist)):
        exmlist[i] = exmlist[i][4:-5]
    return exmlist

def do(html):
    ulist = []
    ip_list = fillUnivList(ulist,html)[1::10]
    ip_list = nottd(ip_list)
    #print(nottd(ip_list))
    ports_list = fillUnivList(ulist,html)[2::10]
    ports_list = nottd(ports_list)
    schema_list = fillUnivList(ulist,html)[5::10]
    schema_list = nottd(schema_list)

    # Schema://IP:Port
    result = []
    for i in range(len(ip_list)):
        result.append(schema_list[i] + '://' + ip_list[i] + ':' + ports_list[i])
    #print(result)
    return result

# 国内高匿代理
url1 = 'https://www.xicidaili.com/nn/'
html1 = getHTMLText(url1)

# 国内普通代理
url2 = 'https://www.xicidaili.com/nt/'
html2 = getHTMLText(url2)

# 国内HTTP代理
url3 = 'https://www.xicidaili.com/wn/'
html3 = getHTMLText(url3)

# 国内HTTPS代理
url4 = 'https://www.xicidaili.com/wt/'
html4 = getHTMLText(url4)

# 字典中的key值即为csv中列名
dataframe = pd.DataFrame({'国内高匿代理':do(html1),'国内普通代理':do(html2),'国内HTTP代理':do(html3),'国内HTTPS代理':do(html4)})

# 将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv("G:/fan/2020学期/2020春/大数据实训/0603_爬虫/test.csv", index=False, sep=',', encoding='gbk')