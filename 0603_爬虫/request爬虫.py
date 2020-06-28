import requests

'''
requests.get('http://www.ecar168.cn/xiaoliang/liebiao/2_0.htm',
                params={
                    'username':'zhangsan',
                    'passwd':'123456'
                }
                )
'''

'''response = requests.get('https://baidu.com/s',
                params={
                    'wd':'book',
                    'ie':'utf-8',
                }
                )
print(response)
print(response.encoding)
response.encoding = 'utf-8'
print(response.text)'''


'''response = requests.get('http://www.ecar168.cn/xiaoliang/liebiao/2_0.htm')
print(response)
print(response.encoding)
response.encoding = 'gbk'
print(response.text)'''

headers = {
    'Connection':'keep-alive',
    #模拟浏览器操作
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

session = requests.session()
response1 = requests.get('http://www.ecar168.cn/xiaoliang/liebiao/2_0.htm',headers=headers)

'''print('response.request.headers:',response.request.headers)
print(response.headers['Set-Cookie'])
print('response.headers:',response.headers)'''

print('response1.request.headers:',response1.request.headers)
print('response1.cookies:',response1.cookies)

'''
cookies = response.cookies
#后续带cookie的请求
requests.get('',cookies=cookies)'''

response2 = session.get('http://www.ecar168.cn/xiaoliang/liebiao/2_0.htm')

print('response2.request.headers:',response2.request.headers)
print('response2.cookies:',response2.cookies)

