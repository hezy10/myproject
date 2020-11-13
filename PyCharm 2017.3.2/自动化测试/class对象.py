

class Car:
    def __init__(self,mark):
        self.mark =mark

class Store:
    pass

class  Personal:
    def __init__(self,name,money):
        self.name = name
        self.__money = money
        # def showmoney


personal = Personal('jeck',100)
# print(personal.name)
# print(personal)


class Point:
    def __init__(self,x=0,y=0):
        if isinstance(x,int):
            raise ValueError('must a int')







# todo 创建Person类
class Person:
    # 初始化
    def __init__(self,name,age,gender,):
        self.name = name
        self.age = age
        self.gender = gender
    # 创建personInfo方法
    def personInfo(self):
        print('我是{}，年龄{}，性别{}'.format(self.name,self.age,self.gender))


# Student继承Person
class Student(Person):
    def __init__(self,name,age,gender,college,class__):
        # 重写
        super(Student, self).__init__(name,age,gender)
        self.college = college
        self.class__ = class__

    def personInfo(self):
        # 重写
        super().personInfo()
        print('学院是{}，班级是{}'.format(self.college,self.class__))

    def study(self,obj):
        # 判断输入的是否为obj格式
        if not isinstance(obj,Teacher):
            raise ValueError('传入的参数需要是Teacher对象')
        print('老师%s,我终于学会了！'%obj.teachObj())

    def __str__(self):
        # 返回的必须是字符串
        return '%s,%s,%s,%s,%s'%(self.name,self.age,self.gender,self.college,self.class__)


# 创建Teacher类
class Teacher(Person):
    def __init__(self,name,age,gender,college,professional):
        super(Teacher, self).__init__(name,age,gender)
        self.clloege = college
        self.professional = professional
    # def __init__(self,*args):
    #     print(args)
    #     super(Teacher, self).__init__(args[0],args[1],args[2])
    #     self.college = college
    #     self.professional = professional

    def personInfo(self):
        super().personInfo()
        print('学院是%s，专业是%s'%(self.clloege,self.professional))

    def teachObj(self):
        return '今天讲了如何用面向对象设计程序'

tea = Teacher('李四',18,'nan','信息工程','科学技术1班')
tea.personInfo()

student = Student('渣渣辉', 16, 'nan','信电','1班')
student.personInfo()
student.study(tea)
print(Teacher.__mro__)
print('###########################>')
print(student)









class User:
    def __init__(self,first_name,last_name,age):
        self.first = first_name
        self.last = last_name
        self.age = age

    def describe_user(self):
        print('%s,%s,%s'%(self.first,self.last,self.age))

    def greet_user(self):
        print('hello hello hello')

# use = User('张三','张二',30)
# print(use.describe_user())
# print(use.greet_user())
