# coding=utf-8
import requests
import re
# https://tieba.baidu.com/f?kw=%E7%BE%8E%E9%A3%9F
# https://tieba.baidu.com/f?kw=%E7%BE%8E%E9%A3%9F&ie=utf-8&pn=50

kw = input('请输入要爬取的名字：')
pn = int(input('要爬取的页数：'))
for i in range(1,pn+1):
    # todo 组装URL地址，获取列表页数据
    response = requests.get(url='https://tieba.baidu.com/f?',params={'kw':kw,'pn':(i-1)*50})
    print(response.url)
    # todo 获取str类型的页面
    ret = response.text
    # print(ret)
    #
    re_pat = '<a rel="noreferrer" href="(.*)" title=".*" target="_blank" class="j_th_tit ">.*</a>'
    pat_list = re.findall(re_pat,ret)
    # print(pat_list)
    # todo 将列表页的详情页
    for i in pat_list:
        htt = 'https://tieba.baidu.com'+i
        print(htt)