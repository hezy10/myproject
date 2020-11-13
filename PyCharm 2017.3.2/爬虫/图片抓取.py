import requests

# url = 'http://tiebapic.baidu.com/forum/abpic/item/8d2f9c5494eef01f0473d59ef7fe9925bd317da2.jpg'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '85.0.4183.83 Safari/537.36'
}

# ret = requests.get(url,headers=headers)
# print(ret.content)
# with open('pa.jpg','wb+') as f:
#     f.write(ret.content)

url = 'https://tieba.baidu.com/f?kw=%E7%BE%8E%E9%A3%9F'
ret = requests.get(url,headers=headers)
print(ret.text)