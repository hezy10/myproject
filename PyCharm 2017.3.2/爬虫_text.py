import requests
from lxml import etree
import pandas as pd

url = 'https://hz.lianjia.com/zufang/'

ret = requests.get(url)
# html = requests.get(url).text
print(ret)

html = ret.text
# print(html)
html_doc = etree.HTML(html)
# //div[@class='content__list']/div/div/span/em
# //div[@class='content__list']/div/div/p[2]/a
node_list = html_doc.xpath("//div[@class='content__list']")

for i in node_list:
    dict_list = {}
    i_price = i.xpath("./div[1]/div[1]/span/em/text()")
    i_position = i.xpath("./div[1]/div[1]/p[2]/a/text()")
    # print(i_price)
    # print(i_position)
    dict_list['price'] = i_price
    dict_list['position'] = i_position
    print(dict_list)
# pd.DataFrame(dict_list).to_csv('text.csv')
