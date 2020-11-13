# 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
def file_save():
    str_up = input('请输入内容:')
    data = str_up.upper()
    with open('aaa.txt','w+') as f:
        f.write(data)
        f.close()
file_save()
# f = open('test.txt','w+')
# f.write(data)
# f.close()


# 求0—7所能组成的奇数个数
def an_odd_number():

    pass


# list_1 = []
# i = 0
# while i <= 7:
#     if i % 2 !=0:
#         list_1.append(i)
#     else:
#         continue
#     i +=1
# print(len(list_1))



# list_new = [1 ,2 ,2 ,6 ,3 ,5 ,5 ,6 ,4 ,3 ,4]
# list_new1 = [1,2,3,4,5,6]
# print(set(list_new))
# dict_1 = {}
# for i in list_new:
#     pass





# srt_1 = '123'
# print(srt_1.endswith('3'))


# inp = input('输入内容:')

# while (1):
#   if inp.isalnum() or inp.isalpha():
#       print('输入内容是:',inp)
#
#
#
#   else:
#       print('输入错误')
#       break

# list_str = []
# str_s = 'hello python'
# for i in str_s:
#
#     if i not in list_str:
#         list_str.append(i)
# print(list_str)
# print(list_str)

from collections import Counter
# zip()
# enumerate() 枚举
# ord()