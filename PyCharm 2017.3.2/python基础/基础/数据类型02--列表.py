
# 检索效率高，列表是可变的
# 链表检索效率低，删除和插入效率高
# 队列先进先出，不能只能操作两头
# 栈先进后出
list_1 = []

# 在指定位置插入元素，超出边界在尾部或头部插入元素
list_1.insert(0,1)
print(list_1)

# 增加多个元素
list_1.extend('123')
list_1.extend([1,[2],3])
print(list_1)

# +创建新的列表
print(list_1+[1,2])

# 列表重复,改一个全都改
list_3 = [1,[2,3],4]
print(list_3*3)
# list_3[1][1] = 5
# print(list_3*3)
# x = list_3*3
# for i in x:
#     print(i)
#     print(id(i))

# 复制
# list_2 = list_1.copy()
# print(list_2 == list_1)
# print(list_2 is list_1)

# 反转
list_1.reverse()
print(list_1)
list_4 = [1,3,6,4,2,5]
list_4.sort(key=int,reverse=True)
print(list_4)

# 随机数
import random
# a=random.randint(1,5)
# print(a)
# b = random.randrange(1,10)
# print(b)
# c = random.choice(list_4)
# print(c)
# random.shuffle(list_1)
# print(list_1)
# e = random.sample(range(10),3)
# print(e)
for i in range(5):
    a = random.randrange(0,20)
    print(a)