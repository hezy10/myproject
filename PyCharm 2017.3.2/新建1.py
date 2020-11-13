from typing import List
import time
import numpy as np


#
#
# def maxArea(self, height: List[int]) -> int:
#     max_area = 0
#     temp_area = 0
#     index1 = 0
#     index2 = len(height) - 1
#     while index1 < index2:
#         if height[index1] <= height[index2]:
#             short_height = height[index1]
#             high_height = height[index2]
#             length = index2 - index1
#             temp_area = short_height * length
#             index1 += 1
#         else:
#             short_height = height[index2]
#             high_height = height[index1]
#             length = index2 - index1
#             temp_area = short_height * length
#             index2 -= 1
#         if temp_area >= max_area:
#             temp = temp_area
#             temp_area = max_area
#             max_area = temp
#     return max_area
#
# print()

def max_area(self, height: List[int]):
    area_max = 0
    area_temp = 0
    index1 = 0
    index2 = len(height) - 1
    while index1 < index2:
        if height[index1] <= height[index2]:
            height_short = height[index1]
            lenght = index2 - index1
            area_temp = height_short * lenght
            index1 += 1
        else:
            height_short = height[index2]
            lenght = index2 - index1
            area_temp = height_short * lenght
            index2 -= 1
        if area_temp >= area_max:
            data = area_temp
            area_temp = area_max
            area_max = data
    return area_max


# if __name__ == '__main__':
#     ret = max_area(6, [7, 8, 6, 9, 9, 7])
# print(ret)


# def intToroman(num):
#     num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     roman_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
#     res = ""
#     for i in range(len(num_list)):
#         while num >= num_list[i]:
#             num -= num_list[i]
#             res += roman_list[i]
#     return res


# print(intToroman(88))


# 冒泡排序

def bubbleSort(a):
    for i in range(1, len(a)):  # 每组遍历的次数
        for j in range(0, len(a) - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]  # if成立a[j]和a[j+1]交换数据
    return a


# if __name__ == '__main__':
# print(bubbleSort([1, 3, 2, 6, 5, 4, 8, 7]))


def num(a):
    list_num = []
    number = len(a) * (len(a) - 1) * (len(a) - 2)
    for i in a:
        for j in a:
            for n in a:
                if i != j and i != n and j != n:  # 判断三位是否重复
                    num_1 = i * 100
                    num_2 = j * 10
                    num_3 = n
                    sum_num = num_1 + num_2 + num_3
                    list_num.append(sum_num)
    return list_num, number


if __name__ == '__main__':
    ret1 = num([1, 2, 3, 4])
    # print(ret1)


def extraction():
    for i in range(100):
        for j in range(100):
            temp = i + 100
            temp = j ** 2
            for n in range(100):
                temp1 = temp + 168
                temp1 = n ** 2
            return i


if __name__ == '__main__':
    r = extraction()
    # print(r)


# a+b+c=1000且a**2+b**2=c**2(a,b,c都是自然数)
# 一个算法中语句的执行次数称为语句频度或时间频度，记为（T(n)）
#
#


# def algorithm():
#     starttime = time.time()
#     for a in range(1001):
#         for b in range(1001):
#             for c in range(1001):
#                 if a**2+b**2 ==c**2 and a+b+c==1000:
#                     print('a{},b{},c{}'.format(a,b,c))
#     endtime = time.time()
#     print(endtime-starttime)
# algorithm()


# start_time = time.time()
# for a in range(1001):
#     for b in range(1001-a):
#         c = 1000-a-b
#         if a**2+b**2 == c**2 and a+b+c == 1000:
# print('a:{},b:{},c:{}'.format(a,b,c))


# end_time = time.time()
# print(end_time-start_time)


# def sortnew(num_new):
#     for i in range(1,len(num_new)):
#          for j in range(0,len(num_new)-i):
#              if num_new[j]>num_new[j+1]:
#                  num_new[j],num_new[j+1] = num_new[j+1],num_new[j]
#     return num_new
# print(sortnew([1,6,5]))

# x = int(input('输入x:'))
# y = int(input('输入y:'))
# z = int(input('输入z:'))
# if x > y:
#     temp = x
#     x = y
#     y = temp
# if x > z:
#     temp = x
#     x = z
#     z = temp
# if y > z:
#     temp = y
#     y = z
#     z = temp
# print(x,y,z)

# print((lambda x, y:x if x > y else y)(1,2))

# for i in range(1,10):
#     for j in range(1,10):
#         if j <= i:
#             print('{}*{}={}'.format(i,j,i*j),end=' ')
#     print(' ')

# 将一个正整数分解质因数。例如：输入 90,打印出 90=2*3*3*5


# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# str_1 = input('请输入')
# for i in str_1:
#     if isinstance(i,str):


# 求 s=a + aa + aaa + aaaa + aa...a 的 值 ， 其 中 a 是 一 个 数 字 。 例 如
# 2+22+222+2222+22222(此时，共有 5个数相加 )，几个数相加有键盘控制。

def a(a):
    sum_a = 0
    sum_aa = 0
    for i in range(5):
        sum_a = sum_a + a * 10 ** i
        sum_aa = sum_aa + sum_a
    return sum_aa


# print(a(2))


# 一球从 100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
# 第 10 次落地时，共经过多少米？第 10 次反弹多高
def high(h, n):
    """

    :param h: 输入下落高度h
    :param n: 反弹次数n
    :return:
    """
    sum1 = 0
    for i in range(n):  # 反弹n次
        h = float(h / 2)  # 转换成浮点型
        sum1 = sum1 + h
    print(sum1)


# if __name__ == '__main__':
# high(100, 10)


# 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃
# 了一个第二天早上又将剩下的桃子吃掉一半， 又多吃了一个。 以后每天早上都吃了前一
# 天剩下的一半多一个。到第 10 天早上想再吃时，见只剩下一个桃子了。求第一天共摘
# 了多少。
def peach(a):
    if a == 1:
        return 1
    else:
        return (peach(a - 1) + 1) * 2  # 第二天的数量加一乘二等于第一天的桃子的总数


# if __name__ == '__main__':
# print(peach(10))

# 两个乒乓球队进行比赛，各出三人。甲队为 a,b,c 三人，乙队为 x,y,z 三人。已
# 抽签决定比赛名单。 有人向队员打听比赛的名单。 a 说他不和 x 比，c 说他不和 x,z 比，
# 请编程序找出三队赛手的名单


def theLotteryGame():
    list_b = ['x', 'y', 'z']
    for i in list_b:
        for j in list_b:
            for k in list_b:
                if i != 'x' and k != 'x' and k != 'z' and i != j and i != k and j != k:
                    # i表示a的对手，j表示b的对手，k表示c的对手，abc的对手不能重复
                    print('a对{},b对{},c对{}'.format(i, j, k))


# if __name__ == '__main__':
#     theLotteryGame()

# 有一分数序列： 2/1，3/2，5/3，8/5，13/8，21/13... 求出这个数列的前 20 项
# 之和。


def sumFraction(n):
    a1 = 1
    b1 = 2
    sum_1 = 0
    for i in range(n):
        c = b1 / a1
        temp = a1
        a1 = b1
        b1 = b1 + temp
        sum_1 = sum_1 + c
    # print(sum_1)


if __name__ == '__main__':
    sumFraction(20)


# 求 1+2!+3!+...+20! 的和


def Sum(n):
    i = 1
    sum1 = 0
    a2 = 1
    while i <= n:
        a2 = a2 * i
        sum1 = sum1 + a2
        i += 1
    return sum1


# if __name__ == '__main__':
#     print(Sum(5))

# 利用递归方法求 5!


def ff(x):
    if x == 1:
        return 1
    else:
        return x * ff(x - 1)


# if __name__ == '__main__':
#    print(ff(5))

# 利用递归函数调用方式，将所输入的 5 个字符，以相反顺序打印出来。
# str1 = input('输入字符:')


# def f(x):
#     if x == -1:
#         return ''
#     else:
#         return str1[x] + f(x-1)
# if __name__ == '__main__':
#     print(f(len(str1)-1))

# 有 5 个人坐在一起，问第五个人多少岁？他说比第 4 个人大 2 岁。问第 4 个人岁
# 数，他说比第 3 个人大 2岁。问第三个人，又说比第 2 人大两岁。问第 2个人，说比第
# 一个人大两岁。最后问第一个人，他说是 10 岁。请问第五个人多大？


def age(n):
    if n == 1:
        return 10
    else:
        return age(n - 1) + 2


# if __name__ == '__main__':
#     print(age(5))

# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续
# 判断第二个字母。
'''
Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday
星期一,星期二,星期三,星期四,星期五,星期六,星期天
'''


# str1 = input('输入:')
#
#
# def week():
#     if str1[0] == 'M':
#         print('Monday,星期一')
#     elif str1[0] == 'W':
#         print('Wednesday,星期三')
#     elif str1[0] == 'F':
#         print('Friday,星期五')
#     elif str1[0] == 'T':
#         if str1[1] == 'u':
#             print('Tuesday,星期二')
#         elif str1[1] == 'h':
#             print('Thursday,星期四')
#     elif str1[0] == 'S':
#         if str1[1] == 'a':
#             print('Saturday,星期六')
#         elif str1[1] == 'u':
#             print('Sunday,星期天')
#     else:
#         print('输入错误，找不到该内容')
# if __name__ == '__main__':
#     week()

# 求 100之内的素数


def primeNumber():
    list_h = []
    for i in range(2, 101):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


# if __name__ == '__main__':
#     primeNumber()


# 给一个不多于 5 位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
def number(num):
    a = str(num)
    print(len(a))
    print(a[::-1])


# if __name__ == '__main__':
#     number(123)

# 一个 5 位数，判断它是不是回文数。即 12321 是回文数，个位与万位相同，十位与千位相同。


# 矩阵
list_new = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = np.array(list_new)
# print(arr)
sum1 = 0
for i in range(3):
    sum1 = sum1+arr[i][i]
# print(sum1)


# 杨辉三角


def yh(n):
    listnew = []
    for i in range(n):
        listnew.append([])       # 在listnew列表里面生成n个子列表
        for j in range(n):
            listnew[i].append(0)  # 将子列表的10个元素全部设为0
    for i in range(n):
        listnew[i][0] = 1
        listnew[i][i] = 1        # 把每个子列表的第一位和最后一位设为1
    for i in range(2,n):         # 计算从第3个子列表开始的第2个元素到倒数第2个元素
        for j in range(1, i):
            listnew[i][j] = listnew[i-1][j-1] + listnew[i-1][j]
    for i in range(n):
        for j in range(i + 1):
            print(listnew[i][j],end=' ')
        print('')
# if __name__ == '__main__':
#     yh(15)


# # bin(二进制) oct(八进制) hex(十六进制)
# print(bin(2),bin(3))
# #按位与 &
# print(2&3)
# # 按位或 |
# print(2|3)
# # 用按位取反 ~
# print(~3)
# # 按位异或 ^
# print(2^3)


# 有 n 个人围成一圈，顺序排号。从第一个人开始报数（从 1 到 3 报数），凡报到 3的人退出圈子，
# 问最后留下的是原来第几号的那位。
def report(n):
    a = list(range(1,n+1))
    count = 0
    while len(a)>1:
        b = a[:]
        for i in range(len(b)):
            count +=1
            if count % 3 == 0:
                a.remove(b[i])
    print(a[0])

# if __name__ == '__main__':
#     report(4)

# 海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子凭据分为五份，多了
# 一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分
# 成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只
# 猴子都是这样做的，问海滩上原来最少有多少个桃子


def peach(n,m):
    pass



# 求 0—7 所能组成的奇数个数。


def number():
    s = 4
    SUM = 4
    for i in range(1,9):
        if i == 1:
            SUM = s
        elif i == 2:
            s = s*7
            SUM = SUM+s
        else:
            s = s*8
            SUM = SUM + s
        print(SUM)
number()