# up在某个分区投了3个以上视频，那个分区的人次就加1
import json

kinds = ['鬼畜', '生活', '时尚', '知识', '游戏', '娱乐', '动画', '资讯', '音乐', '舞蹈', '影视', '纪录片', '国创', '数码', '电影']
data = []
for i in range(15):
    kind_data={"name": kinds[i],"value": 0}
    data.append(kind_data)
# 读取数据
file_path = 'vedio_kind.json'
with open(file_path, 'r', encoding='utf-8') as originFile:
    dataset = json.load(originFile)
    for i in range(len(dataset)):
        # 修改data里面的值
        for j in range(15):
            if kinds[j] in dataset[i].keys():
                # 投稿大于3则算一次
                if dataset[i][kinds[j]] > 3:
                    data[j]["value"] += 1
    print(data)

# 写入 JSON 数据
file_out = 'vedio_kind_statistic.json'
with open(file_out, 'w', encoding='utf-8') as f:
    out = json.dumps(data, indent=4, ensure_ascii=False)
    f.write(out)