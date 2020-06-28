import csv
import json

""" UPlist = ['UP粉丝数'] """
# 爬虫爬UP名单的时候顺便print了一个UP名单的列表(Alt+shift+a)
UPlist = ['爱做饭的芋头SAMA', '啊吗粽', '阿幕降临', '波桑吃遍世界', '宝剑嫂', '长歌与小见见', 
            '-纯黑-', '吃货请闭眼', '吃货明3', '潮汕好男人', '嘟督不噶油', '逗川kshadow', 
            '东尼ookii', '电影最TOP', '盗月社食遇记', '倒悬的橘子', '大祥哥来了',       
            '丰兄来了', '芳斯塔芙', '泛式', '孤独的美食基', '尕丶天堂', '花少北丶', 
            '花花与三猫CatLive', '黑桐谷歌', '黑椒墨鱼', '还有一天就放假了', '槐安遗梦',  
            'ilem', '敬汉卿', '杰里德Jared', '记录生活的蛋黄派', '极客湾Geekerwan', 
            '机智的党妹', '狂风桑', '科技美学', '靠谱电竞', '靠脸吃饭的徐大王', 
            'Kevin英语情报局', 'kei和marin', 'KBShinya', '罗汉解说', '刘老师说电影', 
            '泠鸢yousa', '凉风Kaze', '力元君', '老坛胡说', '老师好我叫何同学', 
            '老番茄', '蜡笔和小勋', '拉宏桑', 'LexBurner', '某幻君', 
            '墨韵Moyun', '绵羊料理', '猫店', '马壮实Hera', '努力的Lorre', '纳豆奶奶', 
            'OELoop', '怕上火暴王老菊', '浅澄月', '枪弹轨迹', '起小点是大腿', '齐天大肾余潇洒', 
            '三无Marblue', '水一大魔王', '守护茶茶', '手工耿', '十音Shiyin', '渗透之C君', 
            '神奇的老皮', '神秘店长A', '山下智博', 'STN工作室', '天天卡牌', '我是郭杰瑞', 
            '我是怪异君', '温柔JUNZ', '歪果仁研究协会', '徐大虾咯', '徐大sao', 
            '-欣小萌-', '小片片说大片', '小可儿', '小潮院长', '逍遥散人', 
            '翔翔大作战', '贤宝宝Baby', '远古时代装机猿', '与山0v0', 
            '影视飓风', '伊丽莎白鼠', '痒局长', '=咬人猫=', '朱一旦的枯燥生活', 
            '周六野Zoey', 'zettaranc', '中国BOY超级大猩猩' ]
# UPlist = [ '中国BOY超级大猩猩' ]
# '木鱼水心','中国BOY超级大猩猩'
for item in UPlist:
    file_path = 'data/' + item + '.csv'
    csvfile = open(file_path,'r',encoding='utf_8_sig')
    file_out = 'json1/' + item + '.json'
    jsonfile = open(file_out,'wb')

    # 获取csv第一行
    reader1 = csv.reader(csvfile)
    for row in reader1:
    # do something here with `row`
        fieldnames = row
        print(row)
        break
    # fieldnames = ["title","comment","play","pic","aid","bvid","created","date,time","length","video_review","favorite","coin","share","like"]
    
    reader = csv.DictReader( csvfile, fieldnames)
    
    # indent=4 带格式输出
    # 编码有点麻烦
    out = json.dumps( [ row for row in reader ] , indent=4, ensure_ascii=False)#.encode("utf-8")
   
    # out = json.dumps( [ row for row in reader ] , indent=4)#.encode("utf-8")
    # jsonfile.write(out.decode("unicode-escape").encode())
    jsonfile.write(out.encode())