import json


preUrl = 'https://www.cnbksy.com/literature/entitysearch/'
willWriteFilePath = './1921totalUrl.txt'
willWriteFile = open(willWriteFilePath, "a")
with open("./1921.json", 'r', encoding='utf-8') as fp:
    data_list = json.load(fp)
    print(type(data_list))
    print(len(data_list))
    # print(data_list[0])
    # print(data_list[1])
    # print(type(data_list[1].get('entityId')))
    # print(data_list[1].get('entityId'))
    # print(preUrl + data_list[1].get('entityId'))
    # 遍历这个文件
    for index, value in enumerate(data_list):
        print(index, preUrl + value.get('entityId'))
        willWriteFile.write(preUrl + value.get('entityId'))
        if index != (len(data_list) - 1):
            willWriteFile.write('\n')



