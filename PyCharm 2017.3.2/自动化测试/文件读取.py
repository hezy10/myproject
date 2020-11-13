# import csv
# # 读取csv文件
# data = csv.reader(open('./a.csv','r'))
# for i in data:
#     print(i)

from xml.dom import minidom

data = minidom.parse('./a.xml')
print(data)
# 获取到当前所有的对象
root = data.documentElement
print(root)
# 获取文档元素
print(root.nodeName)
# 获取xml里面元素
print(root.getElementsByTagName('project'))
print(root.getElementsByTagName('name'))

