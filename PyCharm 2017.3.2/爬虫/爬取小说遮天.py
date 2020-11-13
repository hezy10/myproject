# coding=utf-8
import requests
import re
from lxml import etree


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

# 上代理
# proxies = {'http': 'http://8.129.1.86:8080'}   可以用
# proxies = {'http': 'http://221.182.31.54:8080'}
proxies = {'http': 'http://'}
# proxies = {'http':'username:password@182.34.18.76:9999'}
url = 'http://www.baidu.com'
response = requests.get(url=url, headers=headers, proxies=proxies)
print(response)

# url = 'https://www.biquge5200.cc/modules/article/search.php?'
# bookname = input('输入小说名:')
# todo 获取抓取的小说的url
# response = requests.get(url=url, params={'searchkey':bookname}, headers=headers)
# # print(response.url)
# html_str = response.text
# # print(html_str)
# html_doc = etree.HTML(html_str)
# re_path = '<a href="(.*)">大主宰</a>'
# list_url = re.findall(re_path,html_str)
# # print(list_url)
# # todo 获取列表页的url
# html_list_str = requests.get(url=list_url[1],headers=headers).text
# html_list_doc = etree.HTML(html_list_str)
# node_url_list = html_list_doc.xpath("//div[@id='list']//dd/a/@href")
# # print(node_url_list)
# print(len(node_url_list))
# f = open(bookname+'.txt','a+',encoding='utf-8')
# for node in node_url_list:
#     # todo 抓取小说具体的内容
#     txt_html_str = requests.get(node,headers).text
#     txt_html_doc = etree.HTML(txt_html_str)
#     txt = ''.join(txt_html_doc.xpath("//div[@id='content']/p/text()"))
#     # todo 将内容追加到bookname.txt中
#     f.write(txt)
#
# f.close()
