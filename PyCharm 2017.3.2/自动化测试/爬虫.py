import requests
from lxml import etree
import pandas as pd

start = int(input('起始页面:'))
end = int(input('结束页面:'))

for i in range(start, end + 1):
    print(i)

    url = r'https://hz.qk365.com/list/p' + str(i)
# url = 'https://www.baidu.com'
    print(url)
    # 2、获取当前的请求方式（git）
    # 3、伪造请求requests,获取响应对象
    ret = requests.get(url)
    print(ret)
    html_text = ret.text
    html_doc = etree.HTML(html_text)
    # 4、text获取响应的内容
    print(ret.text)
    # 获取图片，视频
    # print(ret.content)

    # 5、将字符串转换成HTML文档
    # html = etree.HTML(str_html)

    # # todo 寻找每个房间的价格
    # data = html.xpath("//ul[@class='easyList']/li/div/div/div/span/i/text()")
    # print(data)
    # print(len(data))
    #
    # # todo 寻找每个房间地址
    # data_1 = html.xpath("//div[@class='clearfix']/div/p/span/a/text()")
    # print(data_1)
    # print(len(data_1))

    # 6、获取每个li结点，方便获取数据
    # node_list = html_doc.xpath("//ul[@class='easyList']/li")
    # # print(node_list)
    # # print(len(node_list))
    #
    # # 创建列表
    # room_list = []
    # # 循环遍历
    # for item in node_list:
    #     new_dict = {}
    #     item_price = item.xpath('./div[2]/div/div[2]/span/i/text()')
    #     item_position = item.xpath('./div[2]/div[1]/div/p/span/a/text()')
    #     # print(item_price)
    #     # print(item_position)
    #     new_dict['price'] = item_price
    #     new_dict['position'] = item_position
    #     print(new_dict)
    #     # 把获取到的数据追加到room_list中
    #     room_list.append(new_dict)
    #     # 先转成dataframe对象再转成csv文件
    # data = pd.DataFrame(room_list).to_csv(r'text'+str(i)+'.csv')
    # print(data)



'''
requests......请求
node.....结点
price......价格
position......位置
response......响应
Content.......内容
'''
