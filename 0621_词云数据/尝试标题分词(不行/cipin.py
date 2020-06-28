import jieba.analyse
import json

UPlist = ['歪果仁研究协会']

for item in UPlist:
    path = 'title_result/'+ item +'.txt'
    file_in = open(path, 'r', encoding='utf-8')
    content=file_in.read()

    dataCloud = []

    try:
        jieba.analyse.set_stop_words('停用词表.txt')
        tags = jieba.analyse.extract_tags(content, topK=25, withWeight=True)
        for v, n in tags:
            #权重是小数，为了凑整，乘了一万
            print (v + '\t' + str(int(n*10000)))
            # {"name": "Xi's Moments","value": "2020"}
            dataset={"name": v,"value": int(n*10000)}
            dataCloud.append(dataset)

    finally:
        file_in.close()
    
    print(dataCloud)
    data = {"dataCloud":dataCloud}
    # 写入 JSON 数据
    file_out = 'title_json/'+ item +'.txt'
    with open(file_out, 'w', encoding='utf-8') as f:
        out = json.dumps(data, indent=4, ensure_ascii=False)
        f.write(out)