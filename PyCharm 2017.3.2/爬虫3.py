import requests
from lxml import etree


def administrative_num(num):
    url = 'https://xingzhengquhua.51240.com/' + str(num) + '0000000000__xingzhengquhua/'
    ret = requests.get(url)
    print(ret)
    html = ret.text
    doc = etree.HTML(html)
    data = doc.xpath("//tr/td/a/text()")
    print(data)


list_new = [11,12,13,14,15,21,22,23,31,32,33,34,35,36,37,41,42,43,44,45,46,50,51,52,53,54,61,62,63,64,65]
for i in list_new:
    administrative_num(i)
