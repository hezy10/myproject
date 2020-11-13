# ###################set可用于去重操作#######################

set_new = {1, 2, 3, 6}
# print(set_new)


# 去重
# list_new = [4,5,6,7,5,1,2,3,3,2,4]
# set_new1 = []
# for item in list_new:
#     if item not in set_new1:
#         set_new1.append(item)
# print(set_new1)

# # 创建空集合
# data = set()
# print(type(data))

# # 集合的查找用in
# print(10 in set_new)
# print(10 not in set_new)

# # 集合增加
# # 增加单个元素
# set_new.add('ade')
#
# # 增加多个元素
# set_new.update('aab')
#
# # 取并集
# ret = set_new.union('awe')
# print(ret)


# 集合删除
set_new1 = set('apple iphone')
print(set_new1)

# # 随机删除集合中的一个元素
# ret = set_new1.pop()
# print(ret)
#
# # 删除指定的元素
# set_new1.remove(' ')
# print(set_new1)

# 删除成员元素，不是成员元素不做任何事情
set_new1.discard('i')
print(set_new1)

