# coding=utf-8
import requests
from lxml import etree
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '85.0.4183.83 Safari/537.36'
}
# url = 'https://hz.lianjia.com/zufang'
url = 'https://hz.lianjia.com/zufang/zufang/HZ2298569620442841088.html'

response = requests.get(url=url,headers=headers)
print(response)
response.encoding = 'utf-8'
txt = response.text
print(txt)
# txt_doc = etree.HTML(txt)
# price = txt_doc.xpath("//div[@class='content__list--item--main']/span/em/text()")
# print(price)
# pat = '<a class="twoline" target="_blank" href="(.*)">'
# '.*</a>'
# url_list = re.findall(pat,txt)
#
# list_url = []
# for lurl in url_list:
#     node = url+lurl
#     list_url.append(node)
#
# print(list_url)

# for page in list_url:
#     page_html_str = requests.get(page).text
#     page_html_doc = etree.HTML(page_html_str)