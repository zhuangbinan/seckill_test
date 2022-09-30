
import json
import requests
import requests.utils
import http.cookiejar

session = requests.session()

ups_dict = {}
with open("fans_top500_20220706.txt", 'r', encoding='utf-8') as fp:
    # i = 0
    for line in fp:
        # i = i+1
        splits = line.split(' ')
        uname = splits[1]
        uid = splits[2]
        if ups_dict.get(uname) is None:
            ups_dict[uname] = uid
print(len(ups_dict))
print(ups_dict)

bilibili_url = 'https://www.bilibili.com'
res2 = requests.request(method='GET', url=bilibili_url)
cookies = requests.utils.dict_from_cookiejar(res2.cookies)
session.cookies = cookies
print(cookies)

# https://api.bilibili.com/x/web-interface/search/type?__refresh__=true&_extra=&context=&page=3&page_size=50&order=fans&duration=&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=科技&qv_id=7acDIFCtUy2jxppg7iky6c106YPuai2u&category_id=&search_type=bili_user&order_sort=0&user_type=0&dynamic_offset=0&preload=true&com2co=true
search_keyword = '科技'
current = 1
size = 50
search_url = "https://api.bilibili.com/x/web-interface/search/type?__refresh__=true&_extra=&context=&page={}&page_size={}&order=fans&duration=&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword={}&qv_id=7acDIFCtUy2jxppg7iky6c106YPuai2u&category_id=&search_type=bili_user&order_sort=0&user_type=0&dynamic_offset=0&preload=true&com2co=true".format(current, size, search_keyword)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br'
}
resp = requests.get(search_url, headers=headers, cookies=cookies)
resp.encoding = 'utf-8'
print(resp)
print(resp.encoding)
text = resp.text
print(text.encode(encoding='utf-8'))
print(text)
loaded = json.loads(resp.text)
print('解析json')
record = loaded.get('data').get('result')
if record[49].get('fans') > 10000:
    print('大于1W FANS的,这1页的数据我才留下')
    print('存储这1页数据到字典')
    for i in record:
        print(i)
        uname2 = i.get('uname')
        mid = i.get('mid')
        if ups_dict.get(uname2) is None:
            ups_dict[uname2] = mid
print(ups_dict)



