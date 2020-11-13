# coding=utf-8
import requests
from lxml import etree
import time
import random

list_111 = ['http://1.198.73.130:9999',
            'http://20.186.110.157:3128',
            'http://124.172.232.49:8010',
            'http://94.127.144.179:43949',
            'http://205.147.101.141:80',
            'http://177.70.79.74:3128',
            'http://163.204.247.158:9999',
            'http://118.24.89.122:1080',
            'http://45.162.72.3:999',
            'http://190.120.248.8:999',
            'http://185.61.92.207:43947',
            'http://190.90.18.174:999',
            'http://58.220.95.32:10174'
            'http://177.75.159.8:8080',
            'http://45.162.130.33:8080',
            'http://200.108.183.2:8080',
            'http://178.128.211.134:6868',
            'http://94.28.93.117:8080',
            'http://123.149.136.60:9999']
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
list1 = []
list2 = []
# 获取要爬取的代理页面的url
for i in range(1,2):
    url_list = 'https://www.kuaidaili.com/free/inha/'+str(i)+'/'
    list1.append(url_list)
for url in list1:
    proxies = random.choice(list_111)
    # 对具体的代理页面进行抓取
    response = requests.get(url=url,headers=headers,proxies={'http':proxies})
    html_str = response.text
    html_doc = etree.HTML(html_str)
    time.sleep(0.1)
    # 获取代理所在的根节点
    node_list = html_doc.xpath("//tbody/tr")
    for node in node_list:
        # 找出ip
        url_ip = ''.join(node.xpath("./td[1]/text()"))
        # 找出端口
        url_port = ''.join(node.xpath("./td[2]/text()"))
        # 将ip和端口进行拼接
        ip_port = url_ip+':'+url_port
        # 拼接成proxies能用的形式
        proxies = 'http://' + ip_port
        list2.append(proxies)
# 将爬取的数据写到文件中
f = open('爬取的ip.csv','w+')
for i in list2:
    f.write(i)
    f.write('\n')
f.close()
