import pymysql
import sqlalchemy

# todo 创建连接

# con = pymysql.connect(host='localhost', charset='utf8', user='root', password='123456', port=3306, database='pachong')
# print(con)
#
# # todo 获取操作句柄
# cur = con.cursor()
# print(cur)

# todo CRUD
# query1 = 'show tables'
# exe = cur.execute(query1)    # execute 执行
# print(cur.fetchall())       # fetchall 获取所有  fetchone 获取一个 fetch 获取
# print(exe)

# query2 = 'select name from userinfo where id = 8'
# ect = cur.execute(query2)
# fetch = cur.fetchall()
# print(fetch)
# query2 = 'select * from goods where id > 1'
# ex = cur.execute(query2)
# # 显示一行数据
# print(cur.fetchone())
# # 显示所有数据
# print(cur.fetchall())

# sql = "insert into userinfo(name,gender,phone,address)" \
#       " values('小余','女','12345678912',1)"
# ret = cur.execute(sql)
#
# con.commit()    # 提交
#
# sql1 = 'select * from userinfo'
# ret1 = cur.execute(sql1)
# print(cur.fetchall())
# # 涉及数据的增删改需要提交/回滚
#
#
# cur.close()
# con.close()

# 参数列表化

# i = input('111:')
# sql注入

# sql2 = 'select * from userinfo where id=%s'%i
# cur.execute(sql2)
# cur.execute('select * from userinfo where id=%s',[i])
# print(cur.fetchall())

