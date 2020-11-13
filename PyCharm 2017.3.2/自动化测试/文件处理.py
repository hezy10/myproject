# f = open('text.txt','w+')
# f.write('hello python')
# f.close()
# temp = '2017-01-02 13:12:12'
# f = open('text.txt','r+')
# print(f.read())
# print(f.readlines())
# print(f.readline())
import copy

# with open('./test_1.txt') as f:
    # while True:
    #     # todo 读取一行文件
    #     data = f.readline()
    #     # print(data)
    #     if len(data) == 0:
    #         break
    #     # todo 判断temp在data中
    #     if temp in data:
    #         print(data)


list_11 = [[1,2,3],12,13,14]
# 引用 本质是地址的传递
# list_12 = list_11
# print(list_11)
# print(list_12)
# 浅拷贝
list_12 = copy.deepcopy(list_11)
# print(list_11)
# print(list_12)
# list_12 = copy.copy(list_11)
# 把子列表里面的第一个元素1替换成0
list_11[0][0] = 0
print(list_11)
print(list_12)

# print(list_11)
# print(list_12)
# print(id(list_11))
# print(id(list_12))
# print(list_12 == list_11)
# print(list_12 is list_11)
# list_1 = [[1,5,6],2,3,4]
# list_2 = list_1.copy()
# list_1[0] = 1
# print(list_1)
# print(list_2)

# list_1[0][0] = 1
