# coding=utf-8
import requests
import re
import pymongo
from lxml import etree
import random
import time
import pymysql

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
con = pymysql.connect(host='localhost', user='root', password='123456', database='pachong', port=3306,
                          charset='utf8')
cur = con.cursor()
# for i in list_111:
#
#     try:
#         response = requests.get('https://www.baidu.com', proxies={'http':i},headers=headers)
#         print(response)
#         # 将能用的ip写入数据库
#         cur.execute('insert into ip values(0,%s)',[i])
#         con.commit()
#     except:
#         print('====')

# cur.close()
# con.close()
list1 = []
list2 = []
for i in range(1,3):
    url_list = 'http://www.xiladaili.com/gaoni/'+str(i)+'/'
    list1.append(url_list)
for url in list1:
    # proxies = random.choice(list_111)
    # 对具体的代理页面进行抓取
    response = requests.get(url=url,headers=headers)
    html_str = response.text
    html_doc = etree.HTML(html_str)
    # 获取代理ip
    node_list = html_doc.xpath("//tr/td[1]/text()")
    for node in node_list:
        # 拼接成proxies能用的形式
        proxies = 'http://' + node
        cur.execute('insert into zuoye values(0,%s)', [proxies])
        con.commit()
        list2.append(proxies)
cur.close()
con.close()

# f = open('爬取的iptt.csv','w+')
# for i in list2:
#     f.write(i)
#     f.write('\n')
# f.close()

# url = 'http://www.xiladaili.com/'
# response = requests.get(url,headers)
# shtml = response.text
# shtml = '''
# D:\Anaconda\anaconda3\python.exe "E:/PyCharm 2017.3.2/爬虫/爬取代理.py"
#
#
# <!doctype html>
# <html lang="zh-CN">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport"
#           content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
#     <meta http-equiv="X-UA-Compatible" content="ie=edge">
#     <meta name="AizhanSEO" content="b4c34ed5593392df73dd1d84f23a27e6">
#     <link rel="shortcut icon" href="http://xiladaili.oss-cn-hangzhou.aliyuncs.com/static/img/favicon.ico">
#
#
#
#             <title>西拉ip代理官网 - 免费ip代理，代理服务器ip,普通web在线网页代理，高匿http系列产品</title>
#
#
#             <meta name="keywords" content="免费代理ip,代理服务器ip,ip代理,http代理,免费代理服务器,高匿代理ip，在线代理服务器，web在线网页代理"/>
#
#
#             <meta name="description"
#                   content="西拉免费代理ip是行业领先的免费ip代理服务器平台，提供大量的开放免费代理服务器ip地址，其中包括http代理、https代理、Socks5和高匿免费网页代理供大家学习研究使用。">
#
#
#
#
#
#
#
#
#
#     <link rel="canonical" href="http://www.xiladaili.com">
#
#
#
#         <meta name="baidu-site-verification" content="g27rDw0Ysb" />
#
#         <meta name="sogou_site_verification" content="4Osp3NL3OA"/>
#
#         <meta name="shenma-site-verification" content="f12775378c91758db51cde26ecf76145_1545215521">
#
#
#
#     <link rel="stylesheet" href=http://xiladaili.oss-cn-hangzhou.aliyuncs.com/static/css/bootstrap.css>
#
#
#     <link rel="stylesheet" href="/static/css/font-awesome.css">
#     <link rel="stylesheet" href=http://xiladaili.oss-cn-hangzhou.aliyuncs.com/static/css/global.css>
#     <link rel="stylesheet" href=http://xiladaili.oss-cn-hangzhou.aliyuncs.com/static/css/base.css>
#
#     <script src="http://xiladaili.oss-cn-hangzhou.aliyuncs.com/static/js/jquery.js"></script>
#
#     <script src="http://xiladaili.oss-cn-hangzhou.aliyuncs.com/static/js/popper.js"></script>
#
#     <script src="http://xiladaili.oss-cn-hangzhou.aliyuncs.com/static/js/bootstrap.js"></script>
#     <script>
#
#         (function () {
#             var bp = document.createElement('script');
#             var curProtocol = window.location.protocol.split(':')[0];
#             if (curProtocol === 'https') {
#                 bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
#             } else {
#                 bp.src = 'http://push.zhanzhang.baidu.com/push.js';
#             }
#             var s = document.getElementsByTagName("script")[0];
#             s.parentNode.insertBefore(bp, s);
#         })();
#     </script>
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#         <script>
# var _hmt = _hmt || [];
# (function() {
#   var hm = document.createElement("script");
#   hm.src = "https://hm.baidu.com/hm.js?9bfa8deaeafc6083c5e4683d7892f23d";
#   var s = document.getElementsByTagName("script")[0];
#   s.parentNode.insertBefore(hm, s);
# })();
# </script>
#
#         <meta name="360-site-verification" content="c20f10d49db7637e8db1539d087820df" />
#
# </head>
# <body>
# <div class="position-relative">
#
#     <div class="w-100 fixed-top">
#         <div class="container" style="padding:0 5px">
#             <header class="masthead" style="vertical-align: center">
#                 <nav class="navbar navbar-dark navbar-expand-md rounded" style="padding:8px 0;">
#                     <h1>
#                         <a class="text-white" href="/">
#                             <img alt="西拉免费代理IP提供免费IP代理服务器" title="西拉免费代理IP提供免费IP代理服务器" width="35" height="35"
#                                  src=http://xiladaili.oss-cn-hangzhou.aliyuncs.com/static/img/xilalogo.png>
#                         </a>
#                     </h1>
#                     <button class="navbar-toggler bg-primary" type="button" data-toggle="collapse"
#                             data-target="#navbarCollapse"
#                             aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
#                         <span style="width:24px;height:24px;" class="navbar-toggler-icon"></span></button>
#
#                     <div class="collapse navbar-collapse" id="navbarCollapse">
#                         <ul id="ul" class="navbar-nav text-md-center nav-justified w-100">
#                             <li class="nav-item"><a class="nav-link"
#                                                     href="/">免费代理IP</a></li>
#                             <li class="nav-item" style="min-width:45px;"><a class="nav-link"
#                                                                             href="/putong/">普通代理IP</a>
#                             </li>
#                             <li class="nav-item" style="min-width:45px;"><a class="nav-link"
#                                                                             href="/gaoni/">高匿代理IP</a>
#                             </li>
#                             <li class="nav-item" style="min-width:45px;"><a class="nav-link"
#                                                                             href="/http/">http代理</a>
#                             </li>
#                             <li class="nav-item" style="min-width:45px;"><a class="nav-link"
#                                                                             href="/https/">https代理</a>
#                             </li>
#                             <li class="nav-item" style="min-width:45px;"><a class="nav-link"
#                                                                             href="/interface/" rel="nofollow">免费API接口</a>
#                             </li>
#                             <li class="nav-item" style="min-width:45px;"><a class="nav-link"
#                                                                             href="/software/" rel="nofollow">软件代理</a>
#                             </li>
#                             <li class="nav-item" style="min-width:45px;"><a class="nav-link"
#                                                                             href="/buy/"  rel="nofollow">赞助购买</a>
#                             </li>
#
#
#                                 <li class="nav-item active mx-2" style="border-radius:5px;min-width:65px">
#                                     <a class="nav-link btn border-white" href="/login/"  rel="nofollow">登录</a>
#                                 </li>
#                                 <li class="nav-item active mx-2" style="border-radius:5px;min-width:65px">
#                                     <a class="nav-link btn border-white" href="/register/"  rel="nofollow">注册</a>
#                                 </li>
#
#                         </ul>
#                     </div>
#                 </nav>
#             </header>
#         </div>
#     </div>
#
#
#
#
#
#             <div class="w-100" id="xilibg" style="position: relative;">
#                 <div class="container h-100">
#                     <div class="row  h-100 align-items-center justify-content-center pt-5">
#                         <div class="col text-md-left text-center" style="color:#ffffff">
#                             <p style="font-size:4rem;letter-spacing:1.5rem">西拉免费代理IP</p>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#
#
#
#
#
#
#
#     <link rel="stylesheet" href=http://xiladaili.oss-cn-hangzhou.aliyuncs.com/static/css/index.css>
#     <style>
#
#     </style>
#
#
#             <div class="container text-center mt-4" style="padding:0 5px;">
#                 <div id="scroll" class="table-wrapper" style="position:relative;">
#                     <a href="http://www.shenjidaili.com/product/http/" rel="nofollow" class="xici_click">
#                         <div class="xici_click_top">
#                             购买专业版
#                         </div>
#                         <div class="xici_click_bottom">
#                             <ul>
#                                 <li>分布式代理服务器池</li>
#                                 <li>海量集群，吞吐高并发</li>
#                                 <li>无IP白名单</li>
#                                 <li>24小时自助提取</li>
#                                 <li>日可使用最大IP量15W</li>
#                                 <li>更快的访问速度</li>
#                                 <li>专属客服服务</li>
#                             </ul>
#                             <div>了解详情</div>
#                         </div>
#                     </a>
#                     <table class="fl-table" style="min-width:840px;">
#                         <thead style="position:relative;">
#                         <tr>
#                             <th colspan="7" style="font-size:20px">国内高匿免费IP代理</th>
#                             <th colspan="1" style="font-size:20px;text-align: right;">
#                                 <a href="/gaoni/" style="color: #ffffff;">更多高匿免费IP代理>></a>
#                             </th>
#                         </tr>
#                         </thead>
#                         <thead>
#                         <tr>
#                             <th scope="col">免费ip代理</th>
#                             <th scope="col">IP匿名度</th>
#                             <th scope="col">IP类型</th>
#                             <th scope="col">IP位置</th>
#                             <th scope="col">响应速度</th>
#                             <th scope="col">存活时间</th>
#                             <th scope="col">最后验证时间</th>
#                             <th scope="col">打分</th>
#                         </tr>
#                         </thead>
#                         <tbody>
#
#                             <tr>
#                                 <td>83.167.73.151:59871</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 福建 宁德 移动 代理ip</td>
#                                 <td>4.1</td>
#                                 <td>439天 12小时 8分钟 25秒</td>
#                                 <td>2020年9月25日 10:45</td>
#                                 <td>242617</td>
#                             </tr>
#
#                             <tr>
#                                 <td>171.35.141.191:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 江西 抚州 联通 代理ip</td>
#                                 <td>1.86</td>
#                                 <td>1小时 37分钟 50秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>12</td>
#                             </tr>
#
#                             <tr>
#                                 <td>123.163.118.206:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 河南 鹤壁 电信 代理ip</td>
#                                 <td>5.27</td>
#                                 <td>3小时 48分钟 55秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>10</td>
#                             </tr>
#
#                             <tr>
#                                 <td>112.111.217.103:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 福建 宁德 联通 代理ip</td>
#                                 <td>1.31</td>
#                                 <td>1天 12小时 1分钟 39秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>19</td>
#                             </tr>
#
#                             <tr>
#                                 <td>171.11.178.227:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 河南 济源 电信 代理ip</td>
#                                 <td>1.21</td>
#                                 <td>20小时 17分钟 57秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>34</td>
#                             </tr>
#
#                             <tr>
#                                 <td>123.169.166.214:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 山东 德州 电信 代理ip</td>
#                                 <td>2.32</td>
#                                 <td>1天 13小时 50分钟 47秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>12</td>
#                             </tr>
#
#                             <tr>
#                                 <td>163.204.245.51:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 广东 汕尾 联通 代理ip</td>
#                                 <td>1.3</td>
#                                 <td>19小时 29分钟 37秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>12</td>
#                             </tr>
#
#                             <tr>
#                                 <td>1.196.177.124:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 河南 洛阳 电信 代理ip</td>
#                                 <td>3.22</td>
#                                 <td>1天 4小时 44分钟 50秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>11</td>
#                             </tr>
#
#                             <tr>
#                                 <td>113.121.37.201:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 山东 烟台 电信 代理ip</td>
#                                 <td>4.2</td>
#                                 <td>3天 21小时 55分钟 48秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>198</td>
#                             </tr>
#
#                             <tr>
#                                 <td>171.11.178.190:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 河南 济源 电信 代理ip</td>
#                                 <td>2.75</td>
#                                 <td>2天 16小时 15分钟 53秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>48</td>
#                             </tr>
#
#                             <tr>
#                                 <td>175.42.128.104:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 福建 南平 联通 代理ip</td>
#                                 <td>1.21</td>
#                                 <td>1天 22小时 45分钟 33秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>25</td>
#                             </tr>
#
#                             <tr>
#                                 <td>1.198.73.129:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 河南 济源 电信 代理ip</td>
#                                 <td>1.17</td>
#                                 <td>1天 4小时 52分钟 26秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>24</td>
#                             </tr>
#
#                             <tr>
#                                 <td>123.169.166.205:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 山东 德州 电信 代理ip</td>
#                                 <td>1.29</td>
#                                 <td>20小时 12分钟 53秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>12</td>
#                             </tr>
#
#                             <tr>
#                                 <td>117.69.152.123:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 安徽 黄山 电信 代理ip</td>
#                                 <td>1.2</td>
#                                 <td>18小时 23分钟 34秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>25</td>
#                             </tr>
#
#                             <tr>
#                                 <td>175.42.128.128:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 福建 南平 联通 代理ip</td>
#                                 <td>1.05</td>
#                                 <td>4小时 25分钟 46秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>12</td>
#                             </tr>
#
#                             <tr>
#                                 <td>1.198.73.130:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 河南 济源 电信 代理ip</td>
#                                 <td>2.33</td>
#                                 <td>3天 4小时 9分钟 12秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>72</td>
#                             </tr>
#
#                             <tr>
#                                 <td>183.166.162.67:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 安徽 黄山 电信 代理ip</td>
#                                 <td>2.68</td>
#                                 <td>19小时 40分钟 43秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>12</td>
#                             </tr>
#
#                             <tr>
#                                 <td>123.55.98.202:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 河南 鹤壁 电信 代理ip</td>
#                                 <td>1.24</td>
#                                 <td>23小时 55分钟 50秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>33</td>
#                             </tr>
#
#                             <tr>
#                                 <td>20.186.110.157:3128</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 广东 潮州 联通 代理ip</td>
#                                 <td>1.39</td>
#                                 <td>7天 9小时 29分钟 2秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>6175</td>
#                             </tr>
#
#                             <tr>
#                                 <td>175.42.122.190:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 福建 宁德 联通 代理ip</td>
#                                 <td>1.07</td>
#                                 <td>15小时 30分钟 38秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>20</td>
#                             </tr>
#
#                             <tr>
#                                 <td>171.35.166.226:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 江西 宜春 联通 代理ip</td>
#                                 <td>2.6</td>
#                                 <td>1小时 48分钟 42秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>34</td>
#                             </tr>
#
#                             <tr>
#                                 <td>163.204.240.57:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 广东 汕尾 联通 代理ip</td>
#                                 <td>1.61</td>
#                                 <td>21小时 34分钟 55秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>34</td>
#                             </tr>
#
#                             <tr>
#                                 <td>178.128.211.134:6868</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 山东 淄博 移动 代理ip</td>
#                                 <td>6.49</td>
#                                 <td>1天 18小时 59分钟 57秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>371</td>
#                             </tr>
#
#                             <tr>
#                                 <td>123.169.97.243:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 山东 淄博 电信 代理ip</td>
#                                 <td>1.18</td>
#                                 <td>3天 20小时 31分钟 35秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>48</td>
#                             </tr>
#
#                             <tr>
#                                 <td>36.249.53.61:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 福建 泉州 联通 代理ip</td>
#                                 <td>1.09</td>
#                                 <td>2小时 3分钟 1秒</td>
#                                 <td>2020年9月25日 10:41</td>
#                                 <td>12</td>
#                             </tr>
#
#                             <tr>
#                                 <td>123.163.116.249:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 河南 鹤壁 电信 代理ip</td>
#                                 <td>1.43</td>
#                                 <td>1天 23小时 16分钟 21秒</td>
#                                 <td>2020年9月25日 10:41</td>
#                                 <td>34</td>
#                             </tr>
#
#                             <tr>
#                                 <td>124.172.232.49:8010</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 广东 广州 新一代/联通/电信 代理ip</td>
#                                 <td>5.58</td>
#                                 <td>9天 23小时 39分钟 22秒</td>
#                                 <td>2020年9月25日 10:40</td>
#                                 <td>1511</td>
#                             </tr>
#
#                             <tr>
#                                 <td>175.42.122.152:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 福建 宁德 联通 代理ip</td>
#                                 <td>1.29</td>
#                                 <td>1天 15小时 46分钟 2秒</td>
#                                 <td>2020年9月25日 10:40</td>
#                                 <td>23</td>
#                             </tr>
#
#                             <tr>
#                                 <td>123.149.136.117:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 河南 洛阳 电信 代理ip</td>
#                                 <td>1.93</td>
#                                 <td>1小时 35分钟 38秒</td>
#                                 <td>2020年9月25日 10:40</td>
#                                 <td>11</td>
#                             </tr>
#
#                             <tr>
#                                 <td>94.28.93.117:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP,HTTPS</td>
#                                 <td>中国 安徽 亳州 电信 代理ip</td>
#                                 <td>6.0</td>
#                                 <td>136天 14小时 49分钟 30秒</td>
#                                 <td>2020年9月25日 10:40</td>
#                                 <td>110690</td>
#                             </tr>
#
#                         </tbody>
#                     </table>
#                 </div>
#                 <div id="scroll" class="table-wrapper table-responsive">
#                     <table class="fl-table" style="min-width:840px;">
#                         <thead>
#                         <tr>
#                             <th colspan="7" style="font-size:20px">国内免费HTTP代理IP</th>
#                             <th colspan="1" style="font-size:20px;text-align: right;">
#                                 <a href="/http/" style="color: #ffffff;">更多HTTP免费IP代理>></a>
#                             </th>
#                         </tr>
#                         </thead>
#                         <thead class="thead-light">
#                         <tr>
#                             <th>免费ip代理</th>
#                             <th>IP匿名度</th>
#                             <th>IP类型</th>
#                             <th>IP位置</th>
#                             <th>响应速度</th>
#                             <th>存活时间</th>
#                             <th>最后验证时间</th>
#                             <th>打分</th>
#                         </tr>
#                         </thead>
#
#                             <tr>
#                                 <td>123.160.1.103:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 河南 洛阳 电信 代理ip</td>
#                                 <td>6.08</td>
#                                 <td>4天 18小时 28分钟 9秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>158</td>
#                             </tr>
#
#                             <tr>
#                                 <td>94.127.144.179:43949</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 河南 信阳 联通 代理ip</td>
#                                 <td>3.85</td>
#                                 <td>9天 23小时 8分钟 50秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>236</td>
#                             </tr>
#
#                             <tr>
#                                 <td>125.110.127.52:9000</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 浙江 温州 电信 代理ip</td>
#                                 <td>3.13</td>
#                                 <td>3小时 50分钟 45秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>10</td>
#                             </tr>
#
#                             <tr>
#                                 <td>125.108.81.232:9000</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 浙江 温州 电信 代理ip</td>
#                                 <td>5.08</td>
#                                 <td>22小时 56分钟 44秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>8</td>
#                             </tr>
#
#                             <tr>
#                                 <td>178.254.152.154:6666</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 海南 白沙 电信 代理ip</td>
#                                 <td>5.93</td>
#                                 <td>7天 8小时 10分钟 5秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>390</td>
#                             </tr>
#
#                             <tr>
#                                 <td>193.150.21.138:8088</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 北京 北京 阿里云 代理ip</td>
#                                 <td>6.51</td>
#                                 <td>51天 6小时 48分钟 39秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>7957</td>
#                             </tr>
#
#                             <tr>
#                                 <td>103.221.254.125:51630</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 广东 中山 睿江科技 代理ip</td>
#                                 <td>3.72</td>
#                                 <td>116天 22小时 53分钟 23秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>10425</td>
#                             </tr>
#
#                             <tr>
#                                 <td>1.20.217.221:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 黑龙江 大庆 联通 代理ip</td>
#                                 <td>4.77</td>
#                                 <td>11小时 19分钟 38秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>58</td>
#                             </tr>
#
#                             <tr>
#                                 <td>205.147.101.141:80</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 湖南 长沙 电信 代理ip</td>
#                                 <td>5.85</td>
#                                 <td>2天 20小时 10分钟 26秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>168</td>
#                             </tr>
#
#                             <tr>
#                                 <td>117.6.255.171:61966</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 台湾 高雄 代理ip</td>
#                                 <td>2.35</td>
#                                 <td>3天 19小时 38分钟 46秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>195</td>
#                             </tr>
#
#                             <tr>
#                                 <td>195.248.241.191:8088</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 陕西 咸阳 电信 代理ip</td>
#                                 <td>4.33</td>
#                                 <td>18天 17小时 11分钟 10秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>711</td>
#                             </tr>
#
#                             <tr>
#                                 <td>103.111.55.58:46204</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 辽宁 大连 教育网 代理ip</td>
#                                 <td>5.65</td>
#                                 <td>1天 6小时 41分钟 0秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>8</td>
#                             </tr>
#
#                             <tr>
#                                 <td>124.158.168.22:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 海南 文昌 电信 代理ip</td>
#                                 <td>5.62</td>
#                                 <td>50天 10小时 49分钟 51秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>4984</td>
#                             </tr>
#
#                             <tr>
#                                 <td>175.42.68.105:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 福建 宁德 联通 代理ip</td>
#                                 <td>4.38</td>
#                                 <td>4小时 27分钟 7秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>9</td>
#                             </tr>
#
#                             <tr>
#                                 <td>175.43.58.17:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 福建 泉州 联通 代理ip</td>
#                                 <td>5.33</td>
#                                 <td>22小时 54分钟 44秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>8</td>
#                             </tr>
#
#                             <tr>
#                                 <td>177.70.79.74:3128</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 云南 临沧 联通 代理ip</td>
#                                 <td>1.9</td>
#                                 <td>51天 17小时 6分钟 2秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>9925</td>
#                             </tr>
#
#                             <tr>
#                                 <td>81.95.226.138:3128</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 辽宁 铁岭 电信 代理ip</td>
#                                 <td>3.87</td>
#                                 <td>45天 13小时 39分钟 21秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>4440</td>
#                             </tr>
#
#                             <tr>
#                                 <td>125.108.127.251:9000</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 浙江 温州 电信 代理ip</td>
#                                 <td>2.72</td>
#                                 <td>10小时 53分钟 11秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>19</td>
#                             </tr>
#
#                             <tr>
#                                 <td>125.108.120.215:9000</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 浙江 温州 电信 代理ip</td>
#                                 <td>1.84</td>
#                                 <td>20小时 15分钟 11秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>11</td>
#                             </tr>
#
#                             <tr>
#                                 <td>163.204.247.158:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 广东 汕尾 联通 代理ip</td>
#                                 <td>2.75</td>
#                                 <td>7天 14小时 15分钟 7秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>83</td>
#                             </tr>
#
#                             <tr>
#                                 <td>72.169.66.205:87</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 河北 衡水 联通 代理ip</td>
#                                 <td>4.06</td>
#                                 <td>11小时 20分钟 36秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>9</td>
#                             </tr>
#
#                             <tr>
#                                 <td>125.108.93.129:9000</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 浙江 温州 电信 代理ip</td>
#                                 <td>2.79</td>
#                                 <td>9小时 42分钟 28秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>11</td>
#                             </tr>
#
#                             <tr>
#                                 <td>60.13.42.175:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 甘肃 平凉 联通 代理ip</td>
#                                 <td>1.73</td>
#                                 <td>11小时 20分钟 23秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>12</td>
#                             </tr>
#
#                             <tr>
#                                 <td>125.108.70.107:9000</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 浙江 温州 电信 代理ip</td>
#                                 <td>0.92</td>
#                                 <td>16小时 27分钟 22秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>25</td>
#                             </tr>
#
#                             <tr>
#                                 <td>118.24.89.122:1080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 四川 成都 腾讯云 代理ip</td>
#                                 <td>5.61</td>
#                                 <td>30天 14小时 25分钟 19秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>40854</td>
#                             </tr>
#
#                             <tr>
#                                 <td>118.175.207.205:61293</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 香港  香港電訊 代理ip</td>
#                                 <td>4.9</td>
#                                 <td>569天 0小时 16分钟 7秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>252111</td>
#                             </tr>
#
#                             <tr>
#                                 <td>45.162.72.3:999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 河南 济源 联通 代理ip</td>
#                                 <td>5.88</td>
#                                 <td>3天 20小时 18分钟 27秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>214</td>
#                             </tr>
#
#                             <tr>
#                                 <td>89.36.195.238:35328</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 广东 深圳 天威视讯 代理ip</td>
#                                 <td>5.87</td>
#                                 <td>2天 5小时 0分钟 29秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>129</td>
#                             </tr>
#
#                             <tr>
#                                 <td>203.176.129.69:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 内蒙古 锡林郭勒 移动 代理ip</td>
#                                 <td>4.71</td>
#                                 <td>44天 11小时 38分钟 16秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>21613</td>
#                             </tr>
#
#                             <tr>
#                                 <td>190.242.98.61:8083</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTP</td>
#                                 <td>中国 上海 上海 移动 代理ip</td>
#                                 <td>1.36</td>
#                                 <td>253天 10小时 25分钟 12秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>277646</td>
#                             </tr>
#
#                     </table>
#                 </div>
#                 <div id="scroll" class="table-wrapper table-responsive">
#                     <table class="fl-table" style="min-width:840px;">
#                         <thead>
#                         <tr>
#                             <th colspan="7" style="font-size:20px">国内免费HTTPS代理IP</th>
#                             <th colspan="1" style="font-size:20px;text-align: right;">
#                                 <a href="/https/" style="color: #ffffff;">更多HTTPS免费IP代理>></a>
#                             </th>
#                         </tr>
#                         </thead>
#                         <thead>
#                         <tr>
#                             <th>免费ip代理</th>
#                             <th>IP匿名度</th>
#                             <th>IP类型</th>
#                             <th>IP位置</th>
#                             <th>响应速度</th>
#                             <th>存活时间</th>
#                             <th>最后验证时间</th>
#                             <th>打分</th>
#                         </tr>
#                         </thead>
#
#                             <tr>
#                                 <td>123.55.106.50:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 河南 鹤壁 电信 代理ip</td>
#                                 <td>6.2</td>
#                                 <td>4天 18小时 40分钟 10秒</td>
#                                 <td>2020年9月25日 10:45</td>
#                                 <td>71</td>
#                             </tr>
#
#                             <tr>
#                                 <td>218.27.221.161:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 吉林 白山 联通 代理ip</td>
#                                 <td>2.62</td>
#                                 <td>2天 1小时 56分钟 57秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>338</td>
#                             </tr>
#
#                             <tr>
#                                 <td>92.86.10.42:42658</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 广西 柳州 移动 代理ip</td>
#                                 <td>6.85</td>
#                                 <td>373天 3小时 39分钟 4秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>157859</td>
#                             </tr>
#
#                             <tr>
#                                 <td>51.178.220.189:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 四川 甘孜 电信 代理ip</td>
#                                 <td>6.08</td>
#                                 <td>9天 2小时 57分钟 56秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>380</td>
#                             </tr>
#
#                             <tr>
#                                 <td>41.72.196.49:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 香港  香港电讯 代理ip</td>
#                                 <td>3.15</td>
#                                 <td>11天 5小时 13分钟 46秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>321</td>
#                             </tr>
#
#                             <tr>
#                                 <td>79.106.231.70:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 四川 成都 腾讯云/国际节点 代理ip</td>
#                                 <td>6.71</td>
#                                 <td>1天 15小时 54分钟 25秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>132</td>
#                             </tr>
#
#                             <tr>
#                                 <td>188.225.177.82:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 山西 晋城 联通 代理ip</td>
#                                 <td>2.52</td>
#                                 <td>110天 14小时 23分钟 23秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>23393</td>
#                             </tr>
#
#                             <tr>
#                                 <td>187.190.53.182:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 宁夏 银川 移动 代理ip</td>
#                                 <td>5.72</td>
#                                 <td>57天 13小时 48分钟 38秒</td>
#                                 <td>2020年9月25日 10:44</td>
#                                 <td>8061</td>
#                             </tr>
#
#                             <tr>
#                                 <td>190.120.248.8:999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 广西 钦州 联通 代理ip</td>
#                                 <td>6.5</td>
#                                 <td>35天 20小时 14分钟 18秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>2316</td>
#                             </tr>
#
#                             <tr>
#                                 <td>175.43.35.34:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 福建 泉州 联通 代理ip</td>
#                                 <td>2.57</td>
#                                 <td>8天 16小时 31分钟 26秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>141</td>
#                             </tr>
#
#                             <tr>
#                                 <td>185.61.92.207:43947</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 浙江 金华 电信 代理ip</td>
#                                 <td>5.88</td>
#                                 <td>14天 1小时 2分钟 22秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>419</td>
#                             </tr>
#
#                             <tr>
#                                 <td>124.158.179.13:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 台湾 屏东 中華電信 代理ip</td>
#                                 <td>5.45</td>
#                                 <td>63天 14小时 43分钟 54秒</td>
#                                 <td>2020年9月25日 10:43</td>
#                                 <td>21414</td>
#                             </tr>
#
#                             <tr>
#                                 <td>193.200.151.69:48241</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 浙江 温州 联通 代理ip</td>
#                                 <td>5.97</td>
#                                 <td>52天 18小时 31分钟 53秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>4774</td>
#                             </tr>
#
#                             <tr>
#                                 <td>123.163.121.198:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 河南 鹤壁 电信 代理ip</td>
#                                 <td>4.38</td>
#                                 <td>1天 0小时 5分钟 52秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>9</td>
#                             </tr>
#
#                             <tr>
#                                 <td>190.90.18.174:999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 上海 上海 联通 代理ip</td>
#                                 <td>6.21</td>
#                                 <td>20天 14小时 40分钟 35秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>998</td>
#                             </tr>
#
#                             <tr>
#                                 <td>162.144.106.161:3838</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 山东 济南 移动 代理ip</td>
#                                 <td>2.53</td>
#                                 <td>55分钟 26秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>19</td>
#                             </tr>
#
#                             <tr>
#                                 <td>202.51.181.82:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 湖北 荆州 联通 代理ip</td>
#                                 <td>4.28</td>
#                                 <td>248天 22小时 18分钟 22秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>82501</td>
#                             </tr>
#
#                             <tr>
#                                 <td>113.194.141.211:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 江西 宜春 联通 代理ip</td>
#                                 <td>1.72</td>
#                                 <td>15小时 14分钟 13秒</td>
#                                 <td>2020年9月25日 10:42</td>
#                                 <td>12</td>
#                             </tr>
#
#                             <tr>
#                                 <td>58.220.95.32:10174</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 江苏 扬州 电信 代理ip</td>
#                                 <td>0.94</td>
#                                 <td>61天 0小时 4分钟 57秒</td>
#                                 <td>2020年9月25日 10:41</td>
#                                 <td>82982</td>
#                             </tr>
#
#                             <tr>
#                                 <td>222.74.73.202:42055</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 内蒙古 赤峰 电信 代理ip</td>
#                                 <td>6.44</td>
#                                 <td>2天 20小时 3分钟 39秒</td>
#                                 <td>2020年9月25日 10:41</td>
#                                 <td>75</td>
#                             </tr>
#
#                             <tr>
#                                 <td>113.194.133.31:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 江西 宜春 联通 代理ip</td>
#                                 <td>1.3</td>
#                                 <td>1天 14小时 16分钟 2秒</td>
#                                 <td>2020年9月25日 10:41</td>
#                                 <td>12</td>
#                             </tr>
#
#                             <tr>
#                                 <td>177.75.159.8:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 四川 甘孜 电信 代理ip</td>
#                                 <td>3.55</td>
#                                 <td>236天 0小时 52分钟 36秒</td>
#                                 <td>2020年9月25日 10:41</td>
#                                 <td>40430</td>
#                             </tr>
#
#                             <tr>
#                                 <td>103.92.213.253:43399</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 四川 内江 联通 代理ip</td>
#                                 <td>5.64</td>
#                                 <td>16天 4小时 22分钟 42秒</td>
#                                 <td>2020年9月25日 10:41</td>
#                                 <td>386</td>
#                             </tr>
#
#                             <tr>
#                                 <td>89.23.198.13:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 广东 汕头 移动 代理ip</td>
#                                 <td>4.21</td>
#                                 <td>9天 7小时 46分钟 22秒</td>
#                                 <td>2020年9月25日 10:41</td>
#                                 <td>805</td>
#                             </tr>
#
#                             <tr>
#                                 <td>175.42.68.216:9999</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 福建 宁德 联通 代理ip</td>
#                                 <td>5.64</td>
#                                 <td>1天 4小时 46分钟 46秒</td>
#                                 <td>2020年9月25日 10:41</td>
#                                 <td>8</td>
#                             </tr>
#
#                             <tr>
#                                 <td>45.162.130.33:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 台湾  中華電信 代理ip</td>
#                                 <td>5.53</td>
#                                 <td>14小时 42分钟 33秒</td>
#                                 <td>2020年9月25日 10:41</td>
#                                 <td>35</td>
#                             </tr>
#
#                             <tr>
#                                 <td>200.108.183.2:8080</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 西藏 拉萨 电信 代理ip</td>
#                                 <td>6.65</td>
#                                 <td>214天 0小时 49分钟 49秒</td>
#                                 <td>2020年9月25日 10:41</td>
#                                 <td>39217</td>
#                             </tr>
#
#                             <tr>
#                                 <td>119.57.108.53:53281</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 北京 北京 联通 代理ip</td>
#                                 <td>6.82</td>
#                                 <td>3天 6小时 48分钟 58秒</td>
#                                 <td>2020年9月25日 10:40</td>
#                                 <td>159</td>
#                             </tr>
#
#                             <tr>
#                                 <td>185.44.229.227:34930</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 北京 北京 腾讯云 代理ip</td>
#                                 <td>5.52</td>
#                                 <td>3天 19小时 14分钟 49秒</td>
#                                 <td>2020年9月25日 10:40</td>
#                                 <td>239</td>
#                             </tr>
#
#                             <tr>
#                                 <td>27.109.116.119:23500</td>
#                                 <td>高匿名ip代理</td>
#                                 <td>HTTPS</td>
#                                 <td>中国 湖南  移动 代理ip</td>
#                                 <td>6.85</td>
#                                 <td>5天 1小时 57分钟 47秒</td>
#                                 <td>2020年9月25日 10:40</td>
#                                 <td>200</td>
#                             </tr>
#
#                     </table>
#                 </div>
#                 <p class="strong" style="color:rgb(162, 165, 166);font-size:15px;">
#                     西拉免费ip代理服务器提示:表中的打分项目是根据每个免费代理服务器的存活时间、每次验证代理ip响应速度、每次验证代理ip丢包率等ip免费代理服务器性能指标的综合指标，一定程度的代表了该免费代理IP服务器的稳定性。
#
#                 </p>
#
#
#                 <div id="scroll" class="table-wrapper table-responsive">
#                     <table class="fl-table" style="">
#                         <thead>
#                         <tr>
#                             <th style="font-size:20px">免费网页代理服务器小知识</th>
#                             <th style="font-size:20px;text-align: right;">
#                                 <a href="/news/" style="color: #ffffff;">更多代理ip小知识>></a>
#                             </th>
#                         </tr>
#                         </thead>
#
#
#
#
#
#
#
#                                 <tr>
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="news_detail/17187" class="news">
#                                             <span class="h6">使用IP代理西拉ip代理,IP质量高,操作简单</span>
#                                             <span>
#                                                 2020年9月24日 10:32</span>
#                                         </a>
#                                     </div>
#                                 </td>
#
#
#
#
#
#
#
#
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="news_detail/17185" class="news" style="">
#                                             <span class="h6">如今可以出示全面服务的免费代理ip服务提供商</span>
#                                             <span>
#                                                 2020年9月24日 09:44</span>
#                                         </a>
#                                     </div>
#                                 </td>
#                                 </tr>
#
#
#
#
#
#
#
#
#                                 <tr>
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="news_detail/17184" class="news">
#                                             <span class="h6">如何应用大量更平稳的http代理</span>
#                                             <span>
#                                                 2020年9月24日 09:40</span>
#                                         </a>
#                                     </div>
#                                 </td>
#
#
#
#
#
#
#
#
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="news_detail/17136" class="news" style="">
#                                             <span class="h6">应用ip代理来网上是一个确保的实际操作</span>
#                                             <span>
#                                                 2020年9月22日 09:59</span>
#                                         </a>
#                                     </div>
#                                 </td>
#                                 </tr>
#
#
#
#
#
#
#
#
#                                 <tr>
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="news_detail/17134" class="news">
#                                             <span class="h6">代理商类型关键所在免费代理服务器web端配备</span>
#                                             <span>
#                                                 2020年9月22日 09:56</span>
#                                         </a>
#                                     </div>
#                                 </td>
#
#
#
#
#
#
#
#
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="news_detail/17133" class="news" style="">
#                                             <span class="h6">爬虫可以在ip不可以应用以后,拆换一个新的ip详细地址</span>
#                                             <span>
#                                                 2020年9月22日 09:54</span>
#                                         </a>
#                                     </div>
#                                 </td>
#                                 </tr>
#
#
#
#
#
#
#
#
#                                 <tr>
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="news_detail/17014" class="news">
#                                             <span class="h6">互联网上有哪些地区常常可以见到免费代理ip的运用?</span>
#                                             <span>
#                                                 2020年9月17日 11:16</span>
#                                         </a>
#                                     </div>
#                                 </td>
#
#
#
#
#
#
#
#
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="news_detail/17012" class="news" style="">
#                                             <span class="h6">客户能够挑选免费代理ip更改ip地址来开展网上访问</span>
#                                             <span>
#                                                 2020年9月17日 10:52</span>
#                                         </a>
#                                     </div>
#                                 </td>
#                                 </tr>
#
#
#
#
#
#
#
#
#                                 <tr>
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="news_detail/17011" class="news">
#                                             <span class="h6">代理服务器ip会起动全自动清理过虑作用</span>
#                                             <span>
#                                                 2020年9月17日 10:35</span>
#                                         </a>
#                                     </div>
#                                 </td>
#
#
#
#
#
#
#
#
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="news_detail/16963" class="news" style="">
#                                             <span class="h6">可靠的代理服务器ip器能够在个人隐私保护上边具有更强的实际效果</span>
#                                             <span>
#                                                 2020年9月15日 11:11</span>
#                                         </a>
#                                     </div>
#                                 </td>
#                                 </tr>
#
#
#                     </table>
#                 </div>
#                 <div id="scroll" class="table-wrapper table-responsive">
#                     <table class="fl-table" style="">
#                         <thead>
#                         <tr>
#                             <th style="font-size:20px">ip代理分享</th>
#                             <th style="font-size:20px;text-align: right;">
#                                 <a href="/shareip/" style="color: #ffffff;">更多ip代理分享>></a>
#                             </th>
#                         </tr>
#                         </thead>
#
#
#
#
#
#
#
#                                 <tr>
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="shareip_detail/17211" class="news">
#                                             <span class="h6">2020年09月25日10时 中国山东http代理分享 - 西拉免费代理ip</span>
#                                             <span>
#                                                 2020年9月25日 10:00</span>
#                                         </a>
#                                     </div>
#                                 </td>
#
#
#
#
#
#
#
#
#
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="shareip_detail/17210" class="news" style="">
#                                             <span class="h6">2020年09月25日09时 中国安徽http代理分享 - 西拉免费代理ip</span>
#                                             <span>
#                                                 2020年9月25日 09:00</span>
#                                         </a>
#                                     </div>
#                                 </td>
#                                 </tr>
#
#
#
#
#
#
#
#
#
#                                 <tr>
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="shareip_detail/17209" class="news">
#                                             <span class="h6">2020年09月25日08时 中国山东http代理分享 - 西拉免费代理ip</span>
#                                             <span>
#                                                 2020年9月25日 08:00</span>
#                                         </a>
#                                     </div>
#                                 </td>
#
#
#
#
#
#
#
#
#
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="shareip_detail/17208" class="news" style="">
#                                             <span class="h6">2020年09月25日07时 中国山东http代理分享 - 西拉免费代理ip</span>
#                                             <span>
#                                                 2020年9月25日 07:00</span>
#                                         </a>
#                                     </div>
#                                 </td>
#                                 </tr>
#
#
#
#
#
#
#
#
#
#                                 <tr>
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="shareip_detail/17207" class="news">
#                                             <span class="h6">2020年09月25日06时 中国福建http代理分享 - 西拉免费代理ip</span>
#                                             <span>
#                                                 2020年9月25日 06:00</span>
#                                         </a>
#                                     </div>
#                                 </td>
#
#
#
#
#
#
#
#
#
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="shareip_detail/17206" class="news" style="">
#                                             <span class="h6">2020年09月25日05时 中国安徽http代理分享 - 西拉免费代理ip</span>
#                                             <span>
#                                                 2020年9月25日 05:00</span>
#                                         </a>
#                                     </div>
#                                 </td>
#                                 </tr>
#
#
#
#
#
#
#
#
#
#                                 <tr>
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="shareip_detail/17205" class="news">
#                                             <span class="h6">2020年09月25日04时 中国浙江http代理分享 - 西拉免费代理ip</span>
#                                             <span>
#                                                 2020年9月25日 04:00</span>
#                                         </a>
#                                     </div>
#                                 </td>
#
#
#
#
#
#
#
#
#
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="shareip_detail/17204" class="news" style="">
#                                             <span class="h6">2020年09月25日03时 中国广东http代理分享 - 西拉免费代理ip</span>
#                                             <span>
#                                                 2020年9月25日 03:00</span>
#                                         </a>
#                                     </div>
#                                 </td>
#                                 </tr>
#
#
#
#
#
#
#
#
#
#                                 <tr>
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="shareip_detail/17203" class="news">
#                                             <span class="h6">2020年09月25日02时 中国江苏http代理分享 - 西拉免费代理ip</span>
#                                             <span>
#                                                 2020年9月25日 02:00</span>
#                                         </a>
#                                     </div>
#                                 </td>
#
#
#
#
#
#
#
#
#
#                                 <td style="padding: 12px 10px;text-align: left;">
#                                     <div id="div_id_notes" class="value">
#                                         <a href="shareip_detail/17202" class="news" style="">
#                                             <span class="h6">2020年09月25日01时 中国安徽http代理分享 - 西拉免费代理ip</span>
#                                             <span>
#                                                 2020年9月25日 01:00</span>
#                                         </a>
#                                     </div>
#                                 </td>
#                                 </tr>
#
#
#
#                     </table>
#                 </div>
#
#             </div>
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     <div class="w-100 bg pt-5 pb-3" style="background:url(http://xiladaili.oss-cn-hangzhou.aliyuncs.com/static/img/footer.jpg)">
#         <div class="text-center" style="font-size: 1rem;color: #fff;">
#
#             <div class="text-center friendly-link" style="margin-bottom: 15px;">
#                 <p style="color:#fff;font-size:1.5rem;margin-bottom: 0;">友情链接</p>
#
#                     <a href="http://www.chaicp.com" style="color: #fff;" target="_blank">备案查询</a>
#                     |
#
#                     <a href="http://www.7x24cc.com" style="color: #fff;" target="_blank">在线客服</a>
#                     |
#
#                     <a href="http://www.idianliang.com/" style="color: #fff;" target="_blank">SEO公司</a>
#                     |
#
#                     <a href="http://www.qinzhiqiang.com" style="color: #fff;" target="_blank">新媒体营销</a>
#                     |
#
#                     <a href="http://www.zhida56.com" style="color: #fff;" target="_blank">配资平台</a>
#                     |
#
#                     <a href="https://www.ti-net.com.cn" style="color: #fff;" target="_blank">呼叫中心</a>
#                     |
#
#                     <a href="http://www.tjjsad.com" style="color: #fff;" target="_blank">危机公关</a>
#                     |
#
#                     <a href="http://www.wxbl.com" style="color: #fff;" target="_blank">微信公众平台开发</a>
#                     |
#
#                     <a href="https://www.qliaozhai.com" style="color: #fff;" target="_blank">手游</a>
#                     |
#
#                     <a href="http://www.sevenseo.cn" style="color: #fff;" target="_blank">德州SEO</a>
#                     |
#
#                     <a href="http://www.visvn.cn" style="color: #fff;" target="_blank">cpa广告联盟</a>
#                     |
#
#                     <a href="https://www.wangshaoguo.cn" style="color: #fff;" target="_blank">生长因子取出</a>
#                     |
#
#                     <a href="http://www.karlos.com.cn" style="color: #fff;" target="_blank">阿里云服务器</a>
#
#
#             </div>
#
#             <p class="mb-1">
#
#                 <a href="/news/" class="strong" style="color:#ffffff">新闻中心</a>
#                 <a href="/shareip/" class="strong" style="color:#ffffff">代理分享</a>
#                 <span style="color: #ffffff">|</span>
#                 <a href="/sitemap.txt" class="strong" style="color:#ffffff">蜘蛛地图</a>
#             </p>
#
#
#
#
#
#
#
#                 <p class="strong mb-1" style="color:#ffffff">
# 全网最大的<a class="text-white" href="/">免费网页代理ip</a>平台，提供大量<a class="text-white" href="/">免费http代理服务器</a>和<a class="text-white" href="/">免费ip代理</a>地址
# </p>
# <p style="color:#ffffff">© 2016 - 2020. 西拉免费代理ip, All rights reserved.</p>
#
#         </div>
#     </div>
#
#
#
#     <a target="_blank" href="http://wpa.qq.com/msgrd?v=3&uin=359824437&site=qq&menu=yes"
#        class="position-fixed text-center qq_contact" rel="nofollow"
#        style="background: #35A5EF;right: 1rem;bottom: 5rem;width: 4.5rem;height: 4.5rem;border-radius: 0.4rem;line-height: 2.7rem;">
#         <img src=http://xiladaili.oss-cn-hangzhou.aliyuncs.com/static/img/qq.png alt="" style="width: 1.75rem;">
#         <span class="d-block" style="color: #fff;font-size: 0.8rem;line-height: 1rem;">在线客服</span>
#     </a>
# </div>
#
# <script>
#     $(document).ready(function () {
#
#
#         $(".fixed-top").addClass("header-css");
#
#         $(function () {
#             $(window).scroll(function () {      //窗口滚动条
#                 var scrollTop = $(this).scrollTop();  //滚动条顶部的位置
#                 if (scrollTop > 40) {     //当滚动条距离顶部大于100时，加入样式
#                     $(".fixed-top").removeClass("header-css").addClass("header-css1");
#
#
#                 }
#                 if (scrollTop < 40) {
#                     $(".fixed-top").addClass("header-css").removeClass("header-css1");
#
#
#                 }
#             });
#         });
#     });
# </script>
#
#
#
#
#
#     <script>
#
#     </script>
#
#
#
# </body>
# </html>
#
# Process finished with exit code 0
#
# '''
# dhtml = etree.HTML(shtml)
# # re_pat = '<td>(.*)</td>'
# # ip = re.findall(re_pat,shtml)
# ip = dhtml.xpath("//tr/td[1]/text()")
# # list1 = []
# # for i in range(0,len(ip),8):
# #     ip1 = ip[i]
# #     list1.append(ip1)
# # print(list1)
# for i in ip:
#     proxies = {'http': 'http://'+i}
#     try:
#         response = requests.get('http://www.baidu.com',proxies=proxies,headers=headers)
#         print(response)
#         print(proxies)
#     except :
#         print('ip不能用')
#
# # 上代理
# # proxies = {'http': 'http://8.129.1.86:8080'}   可以用
# # proxies = {'http': 'http://221.182.31.54:8080'}
# proxies = {'http': 'http://185.36.157.30:8080'}
# # proxies = {'http':'username:password@182.34.18.76:9999'}
# url = 'http://www.baidu.com'
# response = requests.get(url=url, headers=headers, proxies=proxies)
# print(response)
#
#
#
# # resis支持5种数据类型
# # 1、String
# #   1、添加数据
# #       set 键名 值
# #       setex 键名 过期时间 值
# #       mset 键名1 值1 键名2 值2
# #       append 键名 值
# #   2、查看数据
# #       get 键名
# #       键名错误不报错，返回的是nil
# #       mget 键名1 键名2
# #   3、查看键名
# #       keys *
# #   4、删除键名
# #        del 键名
# #        del 键名1 键名2 键名3
# #
# # 2、哈希类型（键值结构）
# #     1、添加数据
# #         hset 键名 值的键名 值
# #         hmset 键名 值1的键名 值1 值2的键名 值2 .....
# #     2、查看数据
# #         hget 键名 值的键名
# #         hmget 键名 值1的键名 值2的键名 ......
# #         hvals 键名
# #     3、删除数据
# #         del 键名
# #         hdel 键名 值的键名
# # 3、列表
# #     1、添加数据
# #         lpush 键名 值1  值2 .....     -----左插入
# #         rpush 键名 值1  值2 .....     -----右插入
# #         linsert 键名 before|after 指定元素 新元素
# #     2、查看数据
# #         lrange 键名 起始位置 结束位置
# #     3、删除数据
# #         del 键名
# #         lrem 键名 次数 指定的值
# #         lrem 键名 0 指定值 ----删除所有指定元素
# #         lrem 键名 >0 指定值 ----从头开始删除指定元素
# #         lrem 键名 <0 指定值 ----从尾部开始删除指定元素
# #
# #
# # 4、集合
# #     1、添加数据
# #         sadd 键名 值1 ......
# #     2、查看数据
# #         smembers 键名
# #     3、删除数据
# #         del 键名
# #         srem 键名 要删除的值
# #     注意点：
# #         1、集合是无序的
# #         2、元素是字符串类型
# #         3、元素是唯一的没有重复
# #         4、集合没有修改操作
# #
# # 5、有序集合
# #     1、添加数据
# #         zadd 键名 权重1 值1 权重2 值2 .....
# #     2、查看数据
# #         zrange 键名 指定范围
# #         zrangbyscore 键名 指定权重范围
# #         zscore 键名 值 查看权重
# #     3、删除数据
#
# f = open('可用ip.txt','w+')
# for i in list_111:
#     f.write(i)
#     f.write('\n')
# f.close()
