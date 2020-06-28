# 单个作品指数Work: 0.3 * play + 0.15 * (like + coin) + 0.1 * (vedio_review + comment + favorite + share)
import csv
import json
import pandas as pd

UPlist = []
# UPlist = ['爱做饭的芋头SAMA', '啊吗粽', '阿幕降临', '波桑吃遍世界', '宝剑嫂']
avidList = []


file_in = 'unConvertResults.json'
originFile = open(file_in,'r',encoding='utf-8')
# file_out = '10avid.json'
# jsonfile = open(file_out,'w',encoding='utf-8')

dataset = json.load(originFile)
for i in range(len(dataset)):
    UPlist.append(dataset[i]['up_name'])

for item in UPlist:
    Work_list = []         #作品指数列表
    Work_avid = []
    up_avid_list = []
    file_path = 'G:/fan/2020学期/2020春/大数据实训/0615_商业价值计算/data/' + item + '.csv'
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
            avid = row[4]                   #avid
            Work = 0.3 * play + 0.15 * (like + coin) + 0.1 * (vedio_review + comment + favorite + share)
            Work_list.append(Work)
            Work_avid.append([Work,avid])
        Work_list.sort(reverse = True)
        # print(Work_list[:10])
        for i in range(len(Work_list[:50])):
            for j in range(len(Work_avid)):
                if Work_list[i] == Work_avid[j][0]:
                    up_avid_list.append(Work_avid[i][1])
        # print(up_avid_list)
        avidList.append(up_avid_list)



# data_dict = {'UPname': UPlist,
#             'avidList': avidList
#             }
# out = json.dumps(data_dict, indent=4, ensure_ascii=False)
# jsonfile.write(out)

# avid0 = []
# avid1 = []
# avid2 = []
# avid3 = []
# avid4 = []
# avid5 = []
# avid6 = []
# avid7 = []
# avid8 = []
# avid9 = []
# for i in range(len(avidList)):
#     avid0.append(avidList[i][0])
#     avid1.append(avidList[i][1])
#     avid2.append(avidList[i][2])
#     avid3.append(avidList[i][3])
#     avid4.append(avidList[i][4])
#     avid5.append(avidList[i][5])
#     avid6.append(avidList[i][6])
#     avid7.append(avidList[i][7])
#     avid8.append(avidList[i][8])
#     avid9.append(avidList[i][9])
avid_member = []
for i in range(50):
    avid_member.append([])
for i in range(len(avidList)):
    # print(len(avidList[i]))
    # print(avidList[i])
    print(UPlist[i])
    for j in range(min(len(avidList[i]),50)):
        avid_member[j].append(str(avidList[i][j]))
    for j in range(len(avidList[i]),50):
        print(j)
        avid_member[j].append('')



dataframe = pd.DataFrame({'UPname':UPlist,
    # 'avid0':avid0,
    # 'avid1':avid1,
    # 'avid2':avid2,
    # 'avid3':avid3,
    # 'avid4':avid4,
    # 'avid5':avid5,
    # 'avid6':avid6,
    # 'avid7':avid7,
    # 'avid8':avid8,
    # 'avid9':avid9
    'avid0':avid_member[0],
    'avid1':avid_member[1],
    'avid2':avid_member[2],
    'avid3':avid_member[3],
    'avid4':avid_member[4],
    'avid5':avid_member[5],
    'avid6':avid_member[6],
    'avid7':avid_member[7],
    'avid8':avid_member[8],
    'avid9':avid_member[9],
    'avid10':avid_member[10],
    'avid11':avid_member[11],
    'avid12':avid_member[12],
    'avid13':avid_member[13],
    'avid14':avid_member[14],
    'avid15':avid_member[15],
    'avid16':avid_member[16],
    'avid17':avid_member[17],
    'avid18':avid_member[18],
    'avid19':avid_member[19],
    'avid20':avid_member[20],
    'avid21':avid_member[21],
    'avid22':avid_member[22],
    'avid23':avid_member[23],
    'avid24':avid_member[24],
    'avid25':avid_member[25],
    'avid26':avid_member[26],
    'avid27':avid_member[27],
    'avid28':avid_member[28],
    'avid29':avid_member[29],
    'avid30':avid_member[30],
    'avid31':avid_member[31],
    'avid32':avid_member[32],
    'avid33':avid_member[33],
    'avid34':avid_member[34],
    'avid35':avid_member[35],
    'avid36':avid_member[36],
    'avid37':avid_member[37],
    'avid38':avid_member[38],
    'avid39':avid_member[39],
    'avid40':avid_member[40],
    'avid41':avid_member[41],
    'avid42':avid_member[42],
    'avid43':avid_member[43],
    'avid44':avid_member[44],
    'avid45':avid_member[45],
    'avid46':avid_member[46],
    'avid47':avid_member[47],
    'avid48':avid_member[48],
    'avid49':avid_member[49]
    # ,'avidList':avidList
    })
dataframe.to_csv("50avid.csv", index=False, sep=',', encoding='utf_8_sig')