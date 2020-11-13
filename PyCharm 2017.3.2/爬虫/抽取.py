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
    bookname = input('请输入需要查看的小说')

