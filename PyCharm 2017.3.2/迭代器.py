# 迭代是一个访问集合元素的方式
# 迭代器是一个可以记住遍历位置的对象
# 迭代器对象从集合的第一个元素开始访问，直到所有的冤死被访问完结束
# 迭代器只能向前不会后退

# 第一种集合数据类型：列表，元组，字典，集合，字符串等
# 第二种：生成器
# 统称为可迭代对象


from collections.abc import Iterable,Iterator
#
#
# x = [1,2,3,'asd']
# # print(isinstance(x,Iterable))
# # print(isinstance(1000,Iterable))
#
# y = [x for x in range(10)]
# z = (x for x in range(10))
# #
# print(type(y))
# print(type(z))
# # print(isinstance(z,Iterable))
# print(iter(z))
# print(iter(y))
# print(isinstance(iter(y),Iterable))
# print(isinstance(iter(y),Iterator))
# print(isinstance(y,Iterator))
# print('##########################################')
# # 以列表为例，列表是一个可迭代对象，Iter这个方法获取的是列表内部的迭代器
# print(isinstance(z,Iterator))
# print(isinstance(z,Iterable))
# # 生成器是一个迭代器对象，但是列表或者集合等是可迭代的，但是都不是迭代器
# from collections.abc import Iterable, Iterator
#
#
# class MyList(object):
#     def __init__(self):
#         self.newlist = list()
#
#     def append_item(self, data):
#         '''
#         该方法实现了增加一个元素至列表的末尾
#         :param data:
#         :return:
#         '''
#         self.newlist.append(data)
#
#     def __iter__(self):
#         '''当前的类中，因为iter这个魔法方法获取的是__iter__方法中的迭代器'''
#         # 初始化一个迭代器
#         iterobj = MyIterator(self.newlist)
#         return iterobj
#
#
# class MyIterator(object):
#     # 这个类实现的是迭代器类
#     def __init__(self, newlist):
#         self.newlist = newlist
#         # 记录的是当前迭代的索引
#         self.current_index = 0
#
#     def __iter__(self):
#         pass
#
#     def __next__(self):
#         # 当前的魔法方法记录遍历的位置，第二个功能是记录需要获取的值
#         if self.current_index < len(self.newlist):
#             self.current_index += 1
#             return self.newlist[self.current_index - 1]
#
#
# list1 = MyList()
#
#
# print(isinstance(list1,Iterable))
# print(isinstance(iter(list1),Iterator))

# 生成器函数实现

# 斐波拉切数列生成器实现
# def fb(month):
#     m = 0
#     a, b = 0, 1
#     while m < month:
#         yield b
#         a, b = b, a + b
#         m += 1
#         print(b)
#
#
# if __name__ == '__main__':
#     ret = fb(5)
#     print(type(ret))
#     for i in ret:
#         print(i)
    # next(ret)
    # ret.send(None)
    # ret.send(6)
    # while True:
    #     try:
    #         print(next(ret))
    #     except StopIteration:
    #         break


# 闭包


def fun1(num1):

    def inner(num2):
        print(num1,num2)
    return inner
# if __name__ == '__main__':
#     ret = fun1(1)
#     print(ret)


# def linner(k,b):
#
#
#     def inner(x):
#
#         print(k*x+b)
#
#     return inner
# if __name__ == '__main__':
#     f = linner(2,3)
#     f(1)

def wrapper(func):
    def inner():
        # 第一步验证，身份验证
        # 第二步验证，验证是否具有权限
        func()
    return inner
@wrapper
def ordering():

    print('---------------正在下单-------------')
@wrapper
def changepwd():

    print('---------------修改密码-------------')

@wrapper
def showinfo():

    print('---------------个人信息-------------')

# if __name__ == '__main__':
#     # func = wrapper(changepwd)
#     # func()
#     ordering()
#     changepwd()
#     showinfo()


def wrapper1(func):
    print('我是结合性，自下而上')
    def inner(money):
        print('1111')
        func(money)
    print('wrapper1')
    return inner


def wrapper2(func):
    def inner(money):
        print('我是执行性，自上而下')
        print('2222')
        func(money)
    print('wrapper2')
    return inner


# @wrapper2
# @wrapper1
# def changepwd():
#     print('-------修改密码---------')

# @wrapper2
# @wrapper1
# def money(money):
#     print('还有钱',money,'钱')

# if __name__ == '__main__':
#     # changepwd()
#     money(2)

# z = (x for x in range(10))
# for i in z:
#     print(i)

