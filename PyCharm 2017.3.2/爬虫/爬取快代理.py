# coding=utf-8
import requests
import re
from lxml import etree
import time
import pymysql


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}


list1 = []
list2 = []


# 获取要爬取的代理页面的url
for i in range(1,5):
    url_list = 'https://www.kuaidaili.com/free/inha/'+str(i)+'/'
    list1.append(url_list)
a = 0
# 连接数据库设置相关参数
# con = pymysql.connect(host='localhost', user='root', password='123456', database='pachong', port=3306,
#                       charset='utf8')
# # 创建游标
# cur = con.cursor()

for url in list1:
    # 对具体的代理页面进行抓取
    response = requests.get(url=url,headers=headers)
    html_str = response.text
    html_doc = etree.HTML(html_str)
    # 获取代理所在的根节点
    node_list = html_doc.xpath("//tbody/tr")
    a +=1
    list3 = []

    for node in node_list:
        # 找出ip
        url_ip = ''.join(node.xpath("./td[1]/text()"))
        # 找出端口
        url_port = ''.join(node.xpath("./td[2]/text()"))
        # 将ip和端口进行拼接
        ip_port = url_ip+':'+url_port
        # 拼接成proxies能用的形式
        proxies = 'http://' + ip_port
        # try:
        #     # 检查IP是否能用
        #     response = requests.get('http://www.baidu.com', proxies={'http': proxies}, headers=headers)
        #     print(response)
        #     print(proxies)
        #     # 把能用的代理ip写入数据库
        #     cur.execute('insert into ip value(0,%s)',[proxies])
        #     # 提交
        #     con.commit()
        # except:
        #     print('不能使用的ip')
            # 回滚
            # con.rollback()
        list2.append(proxies)
        list3.append(ip_port)

    # f = open('ip.txt','w+')
    # for nod in list3:
    #     proxies = 'http://'+nod
    #     try:
    #         response = requests.get('http://www.baidu.com',proxies={'http':proxies},headers=headers)
    #         print(response)
    #         f.write(proxies['http'])
    #     except:
    #         print('不能使用的ip')
    # f.close()
    print(list3)
    print(len(list3))
    print(a)
# cur.close()
# con.close()
print(list2)
print(len(list2))

# for nod in list2:
#     proxies = 'http://' + nod
#     try:
#         response = requests.get('http://www.baidu.com',proxies={'http':proxies},headers=headers)
#         print(response)
#     except:
#         print('不能使用的ip')


# f = open('ip2.txt','w+')
# for i in list2:
#     f.write(i)
#     f.write('\n')
# f.close()
