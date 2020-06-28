import jieba

UPlist = ['歪果仁研究协会']

for item in UPlist:
    file_in = 'title_txt/'+ item +'.txt'
    data = open(file_in, mode='r', encoding='utf-8')
    file_out = 'title_result/'+ item +'.txt'
    result = open(file_out, mode='w', encoding='utf-8')

    for line in data:
        out = jieba.lcut(line)
        print("/ ".join(out))
        result.write("/ ".join(out))

    result.close()