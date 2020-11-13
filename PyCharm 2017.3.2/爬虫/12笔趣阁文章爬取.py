# coding=utf-8

import requests
from lxml import etree

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

def send_response(url,params=None):
    '''

    :param url: 传入url地址
    :param params:
    :return: 返回doc文档
    '''
    if params is None:
        response = requests.get(url=url,headers=headers)
    else:
        response = requests.get(url=url,headers=headers,params=params)
    response.encoding = 'utf-8'
    html_str = response.text
    html_doc = etree.HTML(html_str)
    return html_doc

def handler_search():
    '''

    :return:
    '''
    bookname = input('请输入需要查看的小说')
    html_doc = send_response('http://www.biquge.info/modules/article/search.php?', params={'searchkey': bookname})
    # todo 获取需要下载书籍页面链接
    href = ''.join(html_doc.xpath("//td[@class='odd']/a/@href"))
    bookurl = 'http://www.biquge.info' + href
    return bookurl,bookname

def handler_detail():
    bookhtml_doc = send_response(bookurl)
    node_list = bookhtml_doc.xpath("//dd/a/@href")
    print(node_list)





# todo  抓取到搜索页面的连接
bookname = input('请输入需要查看的小说')
# url = 'http://www.biquge.info/modules/article/search.php?'
# response = requests.get(url=url,params={'searchkey':bookname},headers=headers)
# response.encoding = 'utf-8'
# html_str = response.text
#
# html_doc = etree.HTML(html_str)
html_doc = send_response('http://www.biquge.info/modules/article/search.php?',params={'searchkey':bookname})

# todo 获取需要下载书籍页面链接
href=''.join(html_doc.xpath("//td[@class='odd']/a/@href"))

bookurl = 'http://www.biquge.info'+href
print(bookurl)
# todo 打开书籍的列表页
# bookresponse = requests.get(url=bookurl,headers=headers)
# bookresponse.encoding = 'utf-8'
# bookhtml = bookresponse.text
# base_url = bookresponse.url
# print(base_url)
# print(bookhtml)

# todo 获取所有的章节链接
# bookhtml_doc = etree.HTML(bookhtml)
bookhtml_doc = send_response(bookurl)
node_list = bookhtml_doc.xpath("//dd/a/@href")

print(node_list)
# # todo  打开详情页，获取页面的数据，写入文件
# f = open(bookname,'a+',encoding='utf-8')
# for node in node_list:
#     # cururl = base_url+node
#     # todo 获取每一个章节的文字部分
#     detail_response = requests.get(url=cururl,headers=headers)
#     detail_response.encoding = 'utf-8'
#     dhtml_str = detail_response.text
#     dhtml_doc = etree.HTML(dhtml_str)
#     txt = ''.join(dhtml_doc.xpath("//div[@id='content']/text()"))
#     # print(txt)
#     f.write(txt)
# f.close()