# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyspiderPipeline:
    def process_item(self, item, spider):
        # print('====================')
        return item

class MyTowPip:
    def process_item(self, item, spider):
        # print('--------------------')
        # print(item)
        return item

# import pymysql
#
# # 创建完class需要到setting中ITEM_PIPELINES注册
# class WriteMysql:
#     def __init__(self):
#         '''
#         连接数据库pachong进行参数的设置host，user，password，database，charset，port
#         '''
#         # todo 连接数据库----connect
#         self.con = pymysql.connect(host='localhost',    # 主机
#                                    user='root',         # 用户
#                                    password='123456',   # 密码
#                                    database='pachong',  # 数据库
#                                    port=3306,           # 接口
#                                    charset='utf8')      # 编码方式
#         # todo 创建游标------cursor
#         self.cur = self.con.cursor()
#
#     def process_item(self, item, spider):
#         try:
#             # todo 将item的cprite和position分别插入到数据库qk表的price和position中
#             self.cur.execute('insert into qk values(0,%s,%s )',(item['cprice'],item['position']))
#             # 插入完成后需要提交，不提交数据库没有数据
#             self.con.commit()
#         except:
#             # 插入失败进行回滚
#             self.con.rollback()
#         return item
#
#     def close_spider(self,spider):
#         # todo 关闭游标
#         self.cur.close()
#         # todo 关闭数据库连接
#         self.con.close()

