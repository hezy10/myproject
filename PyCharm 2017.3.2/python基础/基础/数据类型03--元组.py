t1 = (1,2,3)
print(t1.count(1))
print(t1.index(3))
# 不能修改

# 命名元组
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
a = Point(1,2)
b = Point(3,4)
print(a.x,b.y)
print(a)
S = namedtuple('Student','name,age')
a1 = S('x',10)
print(a1)