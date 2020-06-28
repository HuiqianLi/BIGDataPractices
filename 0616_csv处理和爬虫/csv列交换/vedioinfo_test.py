import csv

# UPlist = ['拉宏桑', 'LexBurner', '某幻君', 
#             '墨韵Moyun', '绵羊料理', '猫店', '马壮实Hera', '努力的Lorre', '纳豆奶奶', 
#             'OELoop', '怕上火暴王老菊', '浅澄月', '枪弹轨迹', '起小点是大腿', '齐天大肾余潇洒', 
#             '三无Marblue', '水一大魔王', '守护茶茶', '手工耿', '十音Shiyin', '渗透之C君', 
#             '神奇的老皮', '神秘店长A', '山下智博', 'STN工作室', '天天卡牌', '我是郭杰瑞', 
#             '我是怪异君', '温柔JUNZ', '歪果仁研究协会', '徐大虾咯', '徐大sao', 
#             '-欣小萌-', '小片片说大片','小潮院长', '逍遥散人', 
#             '翔翔大作战', '贤宝宝Baby', '远古时代装机猿', '与山0v0', 
#             '影视飓风', '伊丽莎白鼠', '痒局长', '=咬人猫=', '朱一旦的枯燥生活', 
#             '周六野Zoey', 'zettaranc']
UPlist = ['中国BOY超级大猩猩']
for item in UPlist:
    file_path = item + '.csv'
    infile = open(file_path,'r', encoding='utf_8_sig')
    file_out = 'result/' + item + '.csv'
    outfile = open(file_out,'w', encoding='utf_8_sig', newline = "")
    originfile = open('潮汕好男人.csv','r', encoding='utf_8_sig')

    reader1 = csv.reader(originfile)
    for row in reader1:
    # do something here with `row`
        fieldnames = row
        break

    # reader2 = csv.reader(infile)
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in csv.DictReader(infile):
        writer.writerow(row)