import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/67.0.3396.79 Safari/537.36'
}
# url = 'https://h5seeds-open.xycdn.com/api/get_seeds'
url = 'https://space.bilibili.com/ajax/member/GetInfo'

# html=requests.get(url,headers)
params = { 
    'name': '爱做饭的芋头SAMA'
    # "mid": "2654670"
}
html = requests.post(url, params)
html.encoding = html.apparent_encoding
print(html.text)

# import requests
# print('访问baidu网站 获取Response对象')
# r = requests.get("http://www.baidu.com")
# print(r.status_code)
# print(r.encoding)
# print(r.apparent_encoding)
# print('将对象编码转换成UTF-8编码并打印出来')
# r.encoding = 'utf-8'
# print(r.text)

