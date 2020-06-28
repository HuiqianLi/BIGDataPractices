import requests
import json
import os
import pandas as pd
import math
import time
import random

class Bilibili_Uvideo():
    def __init__(self, uid):
        self.raw_url = 'https://api.bilibili.com/x/space/arc/search?mid={uid}&pn={page_num}&ps=25&jsonp=jsonp'
        self.uid = uid
        self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        self.total_page = self.get_total_page_num()
        self.video_list = {
            'title':[],       # 标题
            'comment':[],     # 评论数
            'play':[],        # 播放数
            'pic':[],         # 封面链接
            'aid':[],         # a id
            'bvid':[],        # bv id
            'created':[],     # 上传时间戳
            'date':[],        # 上传日期
            'time':[],        # 上传时间
            'length':[],      # 视频长度
            'video_review':[],# 弹幕数量
            'favorite':[],    # 收藏数量
            'coin':[],        # 投币数量
            'share':[],       # 分享数量
            'like':[]         # 点赞数量
        }
        self.up_name = self.get_up_name()
        # print(self.up_name)
        # for i in range(self.total_page):
        # # for i in range(1):
        #     self.reverse_page(i+1)
        #     time.sleep(1)
        # self.save_as_csv()
    
    # getter and setter
    def getTotal_page(self):
        return self.total_page
    
    def setTotal_page(self, new_value):
        self.total_page = new_value

    def get_up_name(self):
        target_url = self.raw_url.format(uid=self.uid, page_num='1')
        hTarget = requests.get(target_url, headers=self.headers)
        js = hTarget.json()
        return js['data']['list']['vlist'][0]['author']

    def get_total_page_num(self):
        target_url = self.raw_url.format(uid=self.uid, page_num='1')
        hTarget = requests.get(target_url, headers=self.headers)
        js = hTarget.json()
        return math.ceil(int(js['data']['page']['count'])/25)

    def reverse_page(self, page_num):
        target_url = self.raw_url.format(uid=self.uid, page_num=page_num)
        hTarget = requests.get(target_url, headers=self.headers)
        js = hTarget.json()
        vlist = js['data']['list']['vlist']
        for i in range(len(vlist)):
            self.video_list['title'].append(vlist[i]['title'])
            self.video_list['comment'].append(vlist[i]['comment'])
            self.video_list['play'].append(vlist[i]['play'])
            self.video_list['pic'].append(vlist[i]['pic'])
            self.video_list['aid'].append(vlist[i]['aid'])
            self.video_list['bvid'].append(vlist[i]['bvid'])
            self.video_list['created'].append(vlist[i]['created'])
            date, _time = self.parse_timestamp(vlist[i]['created'])
            self.video_list['date'].append(date)
            self.video_list['time'].append(_time)
            self.video_list['length'].append(vlist[i]['length'])
            self.video_list['video_review'].append(vlist[i]['video_review'])
            favorite, coin, share, like = self.get_video_detail(vlist[i]['aid'])
            time.sleep(random.randint(100,200)/100)
            self.video_list['favorite'].append(favorite)
            self.video_list['coin'].append(coin)
            self.video_list['share'].append(share)
            self.video_list['like'].append(like)
            # time.sleep(random.randint(50,100)/100)
    
    def save_as_csv(self):
        print(self.video_list['title'])
        df = pd.DataFrame({
            'title':self.video_list['title'],                # 标题
            'comment':self.video_list['comment'],            # 评论数
            'play':self.video_list['play'],                  # 播放数
            'pic':self.video_list['pic'],                    # 封面链接
            'aid':self.video_list['aid'],                    # a id
            'bvid':self.video_list['bvid'],                  # bv id
            'created':self.video_list['created'],            # 上传时间戳
            'date':self.video_list['date'],                  # 上传日期
            'time':self.video_list['time'],                  # 上传时间
            'length':self.video_list['length'],              # 视频长度
            'video_review':self.video_list['video_review'],  # 弹幕数量
            'favorite':self.video_list['favorite'],          # 收藏数量
            'coin':self.video_list['coin'],                  # 投币数量
            'share':self.video_list['share'],                # 分享数量
            'like':self.video_list['like']                   # 点赞数量
        })
        file_name = self.up_name + '.csv'
        file_path = os.path.join('data', file_name)
        df.to_csv(file_path, index=False, sep=',', encoding='utf_8_sig')
    
    def get_video_detail(self, aid):
        video_detail_api = 'https://api.bilibili.com/x/web-interface/archive/stat?aid={aid}'
        target_url = video_detail_api.format(aid=aid)
        hTarget = requests.get(target_url, headers=self.headers)
        data = hTarget.json()['data']
        if data == None:
            return
        else:
            return data['favorite'], data['coin'], data['share'], data['like']
        # except:
        #     print(aid)
        #     return 0, 0, 0, 0
    
    def get_up_detail(self, mid):
        pass

    def parse_timestamp(self, timestamp):
        localtime = time.localtime(timestamp)
        date = str(localtime[0]) + '/' + str(localtime[1]) + '/' + str(localtime[2])
        _time = str(localtime[3]) + ':' + str(localtime[4]) + ':' + str(localtime[5])
        return date, _time

    def generate_breakpoint(self, msg):
        file_name = 'save.data'
        file = open(file_name, 'w')
        file.write(msg)