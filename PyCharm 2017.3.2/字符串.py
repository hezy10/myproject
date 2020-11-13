ret = '今天星期四'
# for i in ret:
    # print(i)

i = 0
while i < len(ret):
    print(ret[i])
    i += 1
# print(ret[0])

# type查看数据类型
# # capitalize将首字母变成大写，其余变成小写
set1 = ret.capitalize()
#
# # index返回字符串出现的最低下标如果不存在就会报错 rindex返回最高下标
# set2 = ret.rindex('i')
#
# count某个字符串出现次数
set3 = ret.count('i')
#
# # find与index相同如果不存在就返回-1，rfind返回最高下标
# set4 = ret.rfind('o')
#
# # upper将所有字母变成大写
# set5=ret.upper()


yel=ret.center(41,'*')
print(yel)

# yel1 = ret.endswith('n')


# yel2 = ret.startswith('t')
# print(yel2)
# print(len(ret))
# print(ret.lower())
sere = ret.encode('utf-8')
sere1 = ret.encode('gbk')
# go = ret.expandtabs()
# print('gbk编码:',sere1)
# print('utf-8编码:',sere)