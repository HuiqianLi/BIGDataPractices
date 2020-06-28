import csv
import json

out = []
count = 0
# 爬虫爬UP名单的时候顺便print了一个UP名单的列表(Alt+shift+a)
UPlist = [ "-欣小萌-",
        "-纯黑-",
        "=咬人猫=",
        "ilem",
        "KBShinya",
        "kei和marin",
        "Kevin英语情报局",
        "LexBurner",
        "OELoop",
        "STN工作室",
        "zettaranc",
        "三无Marblue",
        "与山0v0",
        "东尼ookii",
        "中国BOY超级大猩猩",
        "丰兄来了",
        "伊丽莎白鼠",
        "倒悬的橘子",
        "凉风Kaze",
        "刘老师说电影",
        "力元君",
        "努力的Lorre",
        "十音Shiyin",
        "吃货明3",
        "吃货请闭眼",
        "周六野Zoey",
        "啊吗粽",
        "嘟督不噶油",
        "墨韵Moyun",
        "大祥哥来了",
        "天天卡牌",
        "孤独的美食基",
        "守护茶茶",
        "宝剑嫂",
        "小可儿",
        "小潮院长",
        "小片片说大片",
        "尕丶天堂",
        "山下智博",
        "影视飓风",
        "徐大sao",
        "徐大虾咯",
        "怕上火暴王老菊",
        "我是怪异君",
        "我是郭杰瑞",
        "手工耿",
        "拉宏桑",
        "敬汉卿",
        "木鱼水心",
        "朱一旦的枯燥生活",
        "机智的党妹",
        "杰里德Jared",
        "极客湾Geekerwan",
        "枪弹轨迹",
        "某幻君",
        "槐安遗梦",
        "歪果仁研究协会",
        "水一大魔王",
        "泛式",
        "泠鸢yousa",
        "波桑吃遍世界",
        "浅澄月",
        "渗透之C君",
        "温柔JUNZ",
        "潮汕好男人",
        "爱做饭的芋头SAMA",
        "狂风桑",
        "猫店",
        "电影最TOP",
        "痒局长",
        "盗月社食遇记",
        "神奇的老皮",
        "神秘店长A",
        "科技美学",
        "纳豆奶奶",
        "绵羊料理",
        "罗汉解说",
        "翔翔大作战",
        "老坛胡说",
        "老师好我叫何同学",
        "老番茄",
        "花少北丶",
        "花花与三猫CatLive",
        "芳斯塔芙",
        "蜡笔和小勋",
        "记录生活的蛋黄派",
        "贤宝宝Baby",
        "起小点是大腿",
        "还有一天就放假了",
        "远古时代装机猿",
        "逍遥散人",
        "逗川kshadow",
        "长歌与小见见",
        "阿幕降临",
        "靠脸吃饭的徐大王",
        "靠谱电竞",
        "马壮实Hera",
        "黑桐谷歌",
        "黑椒墨鱼",
        "齐天大肾余潇洒"]
for item in UPlist:
    file_path = 'up_data/' + item + '.csv'
    csvfile = open(file_path,'r',encoding='utf_8_sig')
    file_out = 'vedio_kind.json'
    jsonfile = open(file_out,'w',encoding='utf-8')

    # 获取csv第一行
    reader1 = csv.reader(csvfile)
    for row in reader1:
        fieldnames = row
        # print(fieldnames)
        break
    
    reader = csv.DictReader(csvfile, fieldnames)
    for dct in map(dict, reader):
        for key in dct:
            dct[key] = int(dct[key])
        dct['UPname'] = item
        out.append(json.dumps(dct, ensure_ascii=False))
    
    count += 1
    print(count)

# print(out)
jsonfile.write(str(out))
# 再去转好的文件里,shift+ctrl+f,把'替换成空