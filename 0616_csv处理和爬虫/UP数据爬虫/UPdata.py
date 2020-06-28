import requests
import pandas as pd
from pandas import read_csv
import json
import csv

with open('名单.csv','r',encoding='utf_8_sig') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:#跳过第一行
        break
    mids = [row[0]for row in reader]

# mids = []        #用户ID
name = []       #用户名
face = []       #头像
fans =  []      #粉丝

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/67.0.3396.79 Safari/537.36'
    }

# https://api.bilibili.com/x/web-interface/card?mid={mid}
for mid in mids:
    url = 'https://api.bilibili.com/x/web-interface/card?mid={}'.format(mid)
    response = requests.get(url, headers=headers)
    # print(response.text)

    data = json.loads(response.text)

    code = int(data['code'])
    if code != 0:
        # code不为0则表示结果异常
        response = requests.get(url, headers=headers)
    card = data['data']['card']

    # mid.append(card['mid'])        #用户ID
    name.append(card['name'])      #用户名
    face.append(card['face'])      #头像
    fans.append(card['fans'])      #粉丝

print(name)

dataframe = pd.DataFrame({'mids':mids, 'name':name, 'face': face, 'fans': fans})
dataframe.to_csv("UP粉丝数.csv", index=False, sep=',', encoding='utf_8_sig')
