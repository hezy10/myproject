# coding=utf-8
import requests

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
#                   '85.0.4183.83 Safari/537.36'
# }
#
# url = 'https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action='
#
# ret = requests.get(url,headers)
# ret1 = ret.text
# print(ret1)

import json
dict_l = '{"2": 1, "name": "老王", "d": false, "ed": 18}'
print(json.loads(dict_l))

dict_l = {"2": 1, "name": '老王', "d": False, 'e': None}
sdict = {'老王':'name','None':None,'db':"FALSE"}
print(json.dumps(sdict))
