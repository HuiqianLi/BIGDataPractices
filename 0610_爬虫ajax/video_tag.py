import pandas as pd
import requests
import re
import json


class kfc_home(object):
    def __init__(self):
        aid = '840898516'
        self.url = 'https://api.bilibili.com/x/tag/archive/tags?aid={}'.format(aid)

    def get_page(self):
        # 请求头，浏览器标识
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }

        # 请求的参数
        param = {
            'tag_name': 'tag名称',
            'content': 'tag描述'
        }

        response = requests.get(self.url,headers=headers,params=param)
        try:
            data = json.loads(response.text)['data']
        except Exception:
            # 如果json文件解析失败，重新爬取该页面
            return requests.get(self.url,headers=headers,params=param)
        tag_name = []
        for i in range(len(data)):
            tag_name.append(data[i]['tag_name'])
        print(tag_name)
        # print(data.text)
        return tag_name


if __name__ == "__main__":
    kfc = kfc_home()
    data = kfc.get_page()

# # 字典中的key值即为csv中列名
# dataframe = pd.DataFrame({'国内高匿代理':do(html1),'国内普通代理':do(html2),'国内HTTP代理':do(html3),'国内HTTPS代理':do(html4)})

# # 将DataFrame存储为csv,index表示是否显示行名，default=True
# dataframe.to_csv("test1.csv", index=False, sep=',', encoding='gbk')
