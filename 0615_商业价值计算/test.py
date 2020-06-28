# UP: 粉丝数fans\点赞总数up_like\播放量up_play\发布视频数num
# 人气指数Popularity: 0.35 * fans + 0.35 * up_play + 0.3 * up_like
# 视频: 播放量play\弹幕数vedio_review\投币coin\点赞like\收藏favorite\评论comment\转发share\发布时间create_time
# 单个作品指数Work: 0.3 * play + 0.15 * (like + coin) + 0.1 * (vedio_review + comment + favorite + share)
# 时间系数Xi: 30 / (now_time - create_time) #按天算
# 总作品指数Works: sum( Xi * Work )/num #num个
# 商业价值Business: 0.5 * Popularity + 0.5 * Works
import csv
import datetime
import json

UPlist = []
# UPlist = ['爱做饭的芋头SAMA', '啊吗粽', '阿幕降临', '波桑吃遍世界', '宝剑嫂']
Popularity = []
Works = []
Business = []

fans = []           #粉丝数
up_like = []        #点赞总数
up_play = []        #播放量

file_in = 'unConvertResults.json'
originFile = open(file_in,'r',encoding='utf-8')
file_out = 'BusinessResult.json'
jsonfile = open(file_out,'w',encoding='utf-8')

# {'up_name': '-欣小萌-', 'video_num': 126, 'fans': 2520076, 
# 'comments': 361868, 'plays': 181247888, 'video_reviews': 885737, 
# 'favorites': 2506768, 'coins': 3137828, 'shares': 486473, 'likes': 5564054}, 
dataset = json.load(originFile)
for i in range(len(dataset)):
    UPlist.append(dataset[i]['up_name'])
    fans.append(int(dataset[i]['fans']))
    up_like.append(int(dataset[i]['likes']))
    up_play.append(int(dataset[i]['plays']))


for i in range(len(fans)):
    # 人气指数Popularity
    Popularity.append(int(0.35 * fans[i] + 0.35 * up_play[i] + 0.3 * up_like[i]))

for item in UPlist:
    file_path = 'data/' + item + '.csv'

    Works_list = []         #总作品指数列表
    with open(file_path,'r',encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        # rows = [row for row in reader]
        for row in reader:                  #跳过第一行
            break
        for row in reader:
            if row[2] != '--':
                play = int(row[2])              #播放量
            like = int(row[14])             #点赞
            coin = int(row[12])             #投币
            vedio_review = int(row[10])     #弹幕
            comment = int(row[1])           #评论
            favorite = int(row[11])         #收藏
            share = int(row[13])            #转发/分享
            date = row[7]                   #发布日期2020/5/29
            date_p = datetime.datetime.strptime(date,'%Y/%m/%d').date()
            date_now = datetime.datetime.now().date()
            # print(date_p,date_now)          #<class 'datetime.date'> 2020-05-29
            delta = date_now - date_p       #时间差
            Xi = 30 / int(delta.days)       #时间系数
            Work = 0.3 * play + 0.15 * (like + coin) + 0.1 * (vedio_review + comment + favorite + share)
            Works_list.append(Xi * Work)    #总作品指数计算步骤1

    # 总作品指数Works
    Works.append(int(sum(Works_list)))    #总作品指数计算步骤2

for i in range(len(fans)):
    # 商业价值Business
    Business.append(int(0.5 * Popularity[i] + 0.5 * Works[i]))
    print(i)
    # print(UPlist[i], '人气指数:', Popularity[i])
    # print(UPlist[i], '总作品指数:', Works[i])
    # print(UPlist[i], '商业价值:', Business[i])

data_dict = {'UPname': UPlist,
            'Popularity': Popularity,
            'Works': Works,
            'Business': Business
            }
out = json.dumps(data_dict, indent=4, ensure_ascii=False)
jsonfile.write(out)