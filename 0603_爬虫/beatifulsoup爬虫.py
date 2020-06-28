from bs4 import BeautifulSoup
import requests

# 国内高匿代理

headers = {
    'Connection':'keep-alive',
    #模拟浏览器操作
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
response = requests.get('https://www.xicidaili.com/nn/',headers=headers)

# 构建解析对象，参数1：源数据HTML网页源代码;参数2：解析模式
soup = BeautifulSoup(response.text,'lxml')

# 使用soup对象，获取相应标签及数据
# 1.格式化输出
# print(soup.prettify())

# 2.直接取标签 直接子元素标签
# print(soup.meta)

# 3.通过find函数获取标签
# trs = soup.find_all('tr')
# print(len(trs))
# print(trs)


table = soup.find('table',id="ip_list")
trs = table.find_all('tr')
print(len(trs))
print(trs)


# th = soup.find_all('th',class_="country")
# print(th)

# 4.通过css样式查找标签
# print(soup.select('#ip_list'))
# 实际代码请求的数据里没有tbody,改成'#ip_list > tr:nth-child(2) > td'
# tds = soup.select('#ip_list > tbody > tr:nth-child(2) > td')
'''
tds = soup.select('#ip_list > tr > td')
print(len(tds))
print(tds)
'''

'''table = soup.find('table',id="ip_list")
trs = table.find_all('td')
print(len(trs))
print(trs)'''

'''# 用正则就是模糊查找
pattern = re.compile(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
ips = soup.find_all(text=pattern)
for i in ips:
    print(i)

pattern1 = re.compile(r'HTTPS?')
schemas = soup.find_all(text=pattern1)
for i in schemas:
    print(i)
'''
'''pattern2 = re.compile(r'([0-9]|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])')
ports = soup.find_all(text=pattern2)
for i in ports:
    print(i)'''