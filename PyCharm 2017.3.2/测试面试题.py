# 1、大文件的读取

# f = open('./爬虫/爬取的ip.csv','r')
# op = f.readlines()
# print(op)
# f.close()

# 2、迭代器与生成器的区别
# 迭代是一个访问集合元素的方式
# 迭代器是一个可以记住遍历位置的对象
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束
# 迭代器只能向前不会后退
# 生成器：一边循环，一边计算，生成器是一个返回迭代器的函数，只能用于迭代操作

# 3、装饰器以及装饰器的使用场景
# 接收一个函数作为参数
# 嵌套一个包装函数, 包装函数会接收原函数的相同参数，并执行原函数，且还会执行附加功能
# 返回嵌套函数
# 应用场景：功能扩展，日志，缓存，权限

# 4、对字典中的value排序
dic = {'a':24,'g':52,'l':12,'k':33}
print(sorted(dic.values()))

# 5、分别求出今天是本年本月本周的第几天
year = int(input('请输入正确年份:'))
month = int(input('请输入正确月份:'))
day = int(input('请输入正确日期:'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if (year % 4 ==0 and year % 100 !=0) or (year % 400 == 0):
    print('闰年')
    if 0 < month <=12:
       s = months[month-1]
       days = s + day + 1
       print(days)
       if days % 7 == 0:
           print('周日')
       else:
           print('周{}'.format(days % 7))
    print('本月的第{}天'.format(day))

else:
    if 0 < month <=12:
       s = months[month-1]
       days = s + day
       print(days)
       if days % 7 == 0:
           print('周日')
       else:
           print('周{}'.format(days % 7))
    print('本月的第{}天'.format(day))

# 6、

# 7、

# 8、


# 9、事务特性
# 1、原子性
# 2、一致性
# 3、隔离性
# 4、持久性

# 10、数据库优化查询效率
# 1、对查询进行优化，应尽量避免全表扫描，首先应考虑在 where 及 order by 涉及的列上建立索引
# 2、 应尽量避免在 where 子句中对字段进行 null 值判断，否则将导致引擎放弃使用索引而进行全表扫描
# 3、减少关联查询