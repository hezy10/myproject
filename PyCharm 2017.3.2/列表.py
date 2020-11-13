# list_new = [1,2,3,'456',5,[1,2,3]]
# print(list_new)
# # print(len(list_new))
# # print(list_new[::-1])
# # for i in list_new:
# list_new.append('ab')
# print(list_new)
# list_new.insert(2,'aa')
# print(list_new)
# list_new.extend('apple')
# print(list_new)
# # del list_new
# # print(list_new)
# list_new.pop()
# print(list_new)
# list_new.remove(3)
# print(list_new)
# list_new[2] = 6
# print(list_new)
# print('2' in list_new)
# print(2 not in list_new)
# print(list_new.index(2))
# list_new.reverse()
# print(list_new)
# list_num = [1,22,66,4,3,9,7,555]
# list_num.sort()
# print(list_num)
# ret = list_new.index(3)
# print(ret)
#     print(i)
# # print(list_new)
# #
# #
# # # 创建一个空列表
# # new = list()
# # new1 = []
# #
# #
# # 通过字符串创建列表
# new2 = list('this')
# print(new2)
# #
# # # 列表取值
# # print(list_new[3])
# # print(list_new[:2])
#
# # 循环遍历
# # for i in list_new:
# #     print(i)
#
# # i = 0
# # while i < len(list_new):
# #     print(list_new[i])
# #     # i = i+1
# #     i +=1
#
# # print(len(list_new))
#
#
# # 列表的增删改查
#
#
# # 增加一个数据
# list_new.append('789')
# print(list_new)
# list_new.insert(2,'987')
# print(list_new)
#
#
list_new = [1]
# # 增加多个数据
list_new.extend('123')
list_new.extend([97,[98],99])
# list_new.extend(111)              # 整数和小数不能被迭代
list_new.extend('159')
print(list_new)
#
#
# # 删除单个数据
# # del list_new[2]
# # print(list_new)
# ret = list_new.pop()
# ret2 = list_new.pop()
# print('删除的是:',ret2)
# print(list_new)
# list_new.remove(3)         # 删除第一次出现的值
# print(list_new)
#
#
# # 删除多个数据
# # del list_new
# # print(list_new)
# # list_new.clear()
# # print(list_new)
#
# # 改数据
# list_new[5] = 2
# # list_new.remove(2)
# print(list_new)
#
#
# # 查找数据
# print('22' in list_new)
# print('22' not in list_new)
# ret1 = list_new.index('2')
# ret3 = list_new.count(2)
# print(ret3)
#
#
# # 倒序
# list_new.reverse()
# print(list_new)
#
# # 排序
# text = [2,3,6,1,5,9,7,4]
# text.sort()
# print(text)

# # 输出100以内的偶数
# list_even_number = []
# item = 1
# while item < 100:
#     if item % 2 == 0:
#         list_even_number.append(item)
#     else:
#         pass
#     item += 1
# print(list_even_number)
# print(len(list_even_number))
#
# # 使用while循环输出1 2 3 4 5 6 8 9 10
# list_pr = [1, 2, 3, 4, 5, 6, 8, 9, 10]
# i = 0
# while i < len(list_pr):
#     print(list_pr[i])
#     i += 1
#
# # 求1-100的所有数的和
# i = 1
# sum_add = 0
# while i <= 100:
#     sum_add = sum_add + i
#     i += 1
# print(sum_add)
#
# # 输出 1-100 内的所有奇数
# list_even_number = []
# item = 1
# while item < 100:
#     if item % 2 != 0:
#         list_even_number.append(item)
#     else:
#         pass
#     item += 1
# print(list_even_number)
# # print(len(list_even_number))
#
# # 求1-2+3-4+5 ... 99的所有数的和
# i = 1
# sum_add1 = 0
# while i <100:
#     sum_add1 = ((-1)**(i-1))*i +sum_add1
#     i +=1
# print(sum_add1)