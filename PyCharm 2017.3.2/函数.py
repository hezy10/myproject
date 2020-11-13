# def 函数名():
#     函数体
#     pass          表示补齐结构
def addnum(num1, num2):
    """
    实现两个数的相加
    :param num1: 传入一个数据
    :param num2: 一个数据
    :return: None 没有返回值
    """
    a = num1
    # print('a=', a)
    b = num2
    # print('b=', b)
    c = a + b
    return c


re = addnum(37, 46)
print(re)


# 判断是否是闰年

# year = int(input('请输入年份:'))

def year_new(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):

        print('该年份是闰年')
    else:
        print('该年份不是闰年')


year_new(2020)


# 兔子问题:开始一对兔子，从出生第三个月开始每个月生一对兔子，小兔子长到第三个月每月生一对小兔子，如果兔子不死，
# 每个月兔子有多少对

def rabbit(month):
    if month == 1 or month == 2:
        return 1
    else:
        return rabbit(month - 1) + rabbit(month - 2)


ret = rabbit(5)

print(ret)


# 阶乘
def factorial(num):
    i = 1
    data = 1
    while i <= num:
        data = data * i
        i += 1
    return data


ret1 = factorial(5)

print(ret1)


def factorial_1(num):
    if num == 1:
        return 1
    else:
        return num * factorial_1(num - 1)


ret2 = factorial_1(5)
print(ret2)

# 匿名函数
# lambda 参数:表达式
# 匿名函数的调用方式1
ret_1 = (lambda a, b: a + b)(5, 2)
print(ret_1)
# 匿名函数的调用方式2
f = lambda a,b:a+b
ret_2 = f(1,3)
print(ret_2)