from collections.abc import Iterable,Iterator
# 迭代是一个访问集合元素的方式
# 迭代器是一个可以记住遍历位置的对象
# 迭代器
# x = [1,2,3,4,5]
# # print(isinstance(x,Iterable))
#
# x = [x for x in range(10)]
# y = (x for x in range(10))
# print(isinstance(x,Iterable))
# print(isinstance(y,Iterable))
# print(type(x))
# print(type(y))       #生成器
# print(iter(y))
# print(iter(x))
# print(isinstance(iter(y),Iterator))
# print(isinstance(iter(x),Iterable))
# print(isinstance(x,Iterator))


class MyList(object):
    def __init__(self):
        self.new_list = []

    def app(self,data):
        self.new_list.append(data)

    def __iter__(self):
        iterobj = MyIterator(self.new_list)
        return iterobj


class MyIterator(object):
    def __init__(self,new_list):
        self.new_list = new_list
        # 记录的是当前迭代索引
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # 1记录遍历地位置，2记录需要获取的值
        if self.current_index<len(self.new_list):
            self.current_index +=1
            return self.new_list[self.current_index-1]
        else:
            raise StopIteration


# print(isinstance(iter(MyList()),Iterator))
# print(isinstance(MyList(),Iterable))

a = MyIterator([1,2,3,4,5,6])
# for i in a:
#     print(i)
# for循环原理
# while True:
#     try:
#         value = next(a)
#         print(value)
#     except StopIteration:
#         break


class call:
    def __init__(self,num):
        self.num = num
        self.a = 0
        self.b = 1
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.num:
            result = self.a
            self.a,self.b = self.b,self.a+self.b
            self.current_index +=1
        else:
            raise StopIteration

rb = call(5)
print(rb)



# s = '1123245'
# s.find()