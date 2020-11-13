import requests
import json


# url = 'http://tieba.baidu.com/f/index/forumpark?cn=%E7%BE%8E%E9%A3%9F&ci=380&pcn=%E7%94%9F%E6%B4%BB%E5%AE%B6&pci=214&ct=0&rn=20&pn=1'
# ret = requests.get(url)
# print(ret)
# print(ret.encoding)
# print(ret.headers)

# 伪装成浏览器
header = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
             '85.0.4183.83 Safari/537.36'
}

response = requests.get(url='https://movie.douban.com/j/chart/'
                            'top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20'
                        ,headers=header)
print(response)
# 查看编码方式encoding
print(response.encoding)
# 查看状态码status_code
print(response.status_code)
# 显示url地址
print(response.url)
# content获取字节流文件，多媒体文件
# print(response.content)
# text获取文本文件
print(response.text)
print('---------------------->')
# 编码和解码器
print(response.json())


# json编码
dumps = json.dumps([1,'2',{'he':'风无尘'},None])
print(dumps)
# json解码
loads = json.loads('[1, "2", {"he": "\u98ce\u65e0\u5c18"}, null]')
print(loads)
json.dump(['streaming API'])
# json.load()
#
