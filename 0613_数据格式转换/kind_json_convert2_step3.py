import json

kinds = ['鬼畜', '生活', '时尚', '知识', '游戏', '娱乐', '动画', '资讯', '音乐', '舞蹈', '影视', '纪录片', '国创', '数码', '电影']
# 读取数据
file_path = 'vedio_all_kinds.json'
with open(file_path, 'r', encoding='utf-8') as originFile:
    dataset = json.load(originFile)
    dataset_copy = []#各个UP分区数据合成新列表
    for i in range(len(dataset)):
        dataset_dict = {}#重新整理分区数据的顺序
        UPname = []
        value_list = []
        UPname.append(dataset[i]['UPname'])
        dataset_dict['UPname']=UPname
        dataset_dict['name']=kinds
        for j in range(15):
            value_list.append(dataset[i][kinds[j]])
        dataset_dict['value']=value_list
        dataset_copy.append(dataset_dict)
        # break
    print(dataset_copy)

data = {"data":dataset_copy}
# 写入 JSON 数据
file_out = 'Funnel.json'
with open(file_out, 'w', encoding='utf-8') as f:
    out = json.dumps(data, indent=4, ensure_ascii=False)
    f.write(out)