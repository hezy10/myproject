def factorial_sum(num):
    '''
    求num个阶乘的和
    :param num:
    :return:
    '''
    i = 1
    data = 1
    sum_1 = 0
    while i <= num:
        data = data * i
        sum_1 = sum_1 + data
        i += 1
    return sum_1


# if __name__ == '__main__':
#     print(factorial_sum(20))


def factorial(num):
    '''
    递归法求阶乘
    :param num:
    :return:
    '''
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


# if __name__ == '__main__':
# print(factorial(6))


# def reverse(List):
#     list_1 = []
#     i = 1
#     while i <= len(List):
#         list_1.append(List[i-1])
#         i += 1
#
# if __name__ == '__main__':
#     print(reverse([1,5,3,4]))


def old_man(n):
    '''
    求第n个人的年龄
    :param n:
    :return:
    '''
    old_man = 10
    i = 1
    while i <= n:
        old_man = old_man + 2
        i += 1
    return old_man


# if __name__ == '__main__':
#     print(old_man(4))


def decomposition_factor(num):
    list_prime = []
    while num != 1:
        for i in range(2, num):
            if num % i == 0:
                pass



def screening(a,num):
    list_1 = []
    list_2 = []
    dict_1 = {}
    for i in a:
        if i < num:
            list_1.append(i)
        else:
            list_2.append(i)
        dict_1['key1'] = list_2
        dict_1['key2'] = list_1
    print(dict_1)

# screening([11, 22, 33, 44, 55, 66, 77, 88, 99, 90],50)



def graph(a):
    i = 1
    j = 7
    while i <= 9:
        str_temp = a * i
        print(str_temp.center(11))
        i += 2
    while j <= 7:
        str_temp = a*j
        print(str_temp.center(11))
        j -= 2
        if j == -1:
            break
# graph('*')


from timeit import Timer


def fun1():
    list_1 = []
    for i in range(50000):
        list_1 = list_1+[i]


def fun2():
    list_1 = []
    for i in range(50000):
        list_1 = list_1.append(i)


def fun3():
    list_1 = []
    for i in range(50000):
        list_1 = list_1.insert(0, i)



timer1 = Timer('fun1','from __main__ import fun1')
timer2 = Timer('fun2','from __main__ import fun2')
timer3 = Timer('fun3','from __main__ import fun3')
print('+',timer1.timeit(number=50000))
print('append',timer2.timeit(number=50000))
print('insert',timer3.timeit(number=50000))


def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
ret = bubbleSort([6,5,4,2,3,1])
print(ret)