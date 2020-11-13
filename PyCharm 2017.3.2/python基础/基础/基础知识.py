#
# # 1字节 = 8位
# # //向下取整
# i = 1//2
# print(i)
#
# # 取商和余数
# i = divmod(5,2)
# print(i)
#
# # 按位与&
# print(9 & 8)
#
# # 判断奇偶数 取模或按位相与
# print(9 % 2 ==1)
# print(9 & 1==1)
#
# # 按位相与
# print(9 | 2)
#
# # 移位 左移<<或右移>>
#
# # 右移两位相当于8除以2的平方
# print(8 >> 2)
#
# # 左移相当于乘以2的几次方
# print(8 << 2)
#
# # 异或^、同或
# print(7 ^ 1)
#
# # 补码的补码是原码
#
# # 取反
# print(~12)

# 赋值即定义

# 判断一个是几位数
# # 比较思想
# a = int(input('>>>'))
# if a >= 10000:
#     print('5')
# elif a >= 1000:
#     print('4')

# #  折半思想
# a = 1234
# if a > 1000:
#     if a >= 10000:
#         print('5')
#     else:
#         print('4')
# else:
#     if a > 100:
#         print('3')
#     elif a > 10:
#         print('2')
#     else:
#         print('1')

# 0~10倒序输出
# for i in range(10,0,-1):
#     print(i)
# help(range)

# # 筛选偶数的几种方法
# # 取模运算
# for i in range(10):
#     if i % 2 == 0:
#         print(i)
# # 判断真假
# for i in range(10):
#     if not i % 2:
#         print(i)
# # 判断真假
# for i in range(10):
#     if  not i & 1:
#         print(i)
# # 通过与运算
# for i in range(10):
#     if i & 1 == 0:
#         print(i)
# # 直接遍历
# for i in range(0,10,2):
#     print(i)
# # 通过continue实现
# for i in range(10):
#     if i & 1:
#         continue # 中止当前循环
#     print(i)

# for i in range(100):
#     if i % 7 == 0:
#         print(i)
#
# for i in range(0,100,7):
#     print(i)
#
# for i in range(100):
#     if not i % 7:
#         print(i)
#
# for i in range(100):
#     if i % 7:
#         continue
#     print(i)

# a = 1
# for i in range(7,1000,7):
#     print(i)
#     if a == 10:
#         break    # 终止循环
#     a +=1
#
# print('--------------->')
#
# a = 0
# for i in range(7,1000,7):
#     print(i)
#     a += 1
#     if a == 10:
#         break    # 终止循环
#
# print('---------------->')
#
# b = 7
# for i in range(10):
#     print(b)
#     b += 7


# 逆序打出1到10
for i in range(10,0,-1):
    print(i)

# 依次打印一个五位数的万位到个位
w = 10000
num = 12345
for i in range(5):
    print(num // w)
    num = num % w
    w = w // 10


num = 12345
# 逆序打出
for i in range(5):
    print(num % 10)
    num = num // 10

# 打印001230，1前面的0不要
print('=======')
a = '0000001230'
num = int(a)
w = 10**(len(a)-1)
flag = False  # 标记
for i in range(len(a)):
    t = num // w
    if t:  # t为真时flag为true
        flag = True
    if flag:
        print(t)
    num = num % w
    w = w // 10

# 判断是几位数,依次打印
print('----------')
a = '001234'
num = int(a)
length = 5
w = 10000
flag = False

while 1:
    c = num // w
    if not flag:
        if c:
            flag = True
        else:
            length -= 1  # 如果
    if flag:
        print(c)
    num = num % w
    w = w // 10
    print(length)