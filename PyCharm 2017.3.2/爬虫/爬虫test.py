# coding=utf-8
import requests
from lxml import etree
import time
import pymysql


#定义请求头信息
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

# 连接数据库
con = pymysql.connect(host='localhost',
                      user='root',
                      password='123456',
                      database='pachong',
                      port=3306,
                      charset='utf8')
# 创建游标
cur = con.cursor()
list1 = []

# 要抓取代理列表页的url
for i in range(1,350):
    url_list = 'http://www.xiladaili.com/gaoni/'+str(i)+'/'
    list1.append(url_list)

for url in list1:
    # 对具体的代理页面进行抓取
    response = requests.get(url=url,headers=headers)
    html_str = response.text
    html_doc = etree.HTML(html_str)
    time.sleep(0.1)
    # 获取代理ip
    node_list = html_doc.xpath("//tr/td[1]/text()")

    for node in node_list:
        # 拼接成proxies需要形式
        proxies = 'http://' + node
        # 将拼接好的proxies存到数据库
        cur.execute('insert into zuoye values(0,%s)', [proxies])
        # 提交
        con.commit()

# 关闭游标和数据库连接
cur.close()
con.close()
