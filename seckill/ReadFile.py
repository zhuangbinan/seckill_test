import json


with open("1920totalUrl.txt", 'r', encoding='utf-8') as fp:
    i = 0
    for line in fp:
        i = i+1
        print(i, line)
