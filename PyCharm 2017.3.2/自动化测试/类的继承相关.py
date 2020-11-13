#1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
class Person():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print('{},{},{}'.format(self.name,self.age,self.gender))
# 2、创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，创建方法study参数为Teacher对象，调用Teacher类的teachObj方法，接收老师教授的知识点，然后打印‘老师xxx,我终于学会了！’xxx为老师的teach方法返回的信息。重写__str__方法，返回student的信息。
class Student(Person):
    def __init__(self,name,age,gender,college,class__):
        super(Student, self).__init__(name,age,gender)
        self.class__ = class__
        self.college = college


    def personInfo(self):
        super().personInfo()
        print('学院%s，班级%s'%(self.college,self.class__))


    def study(self,obj):
        if not isinstance(obj,Teacher):
            raise ValueError( '传入的参数必须是Teacher的对象')

        subject = obj.teachObj()
        print('‘老师%s,我终于学会了！’'%subject)

    def __str__(self):
        return '%s,%s,%s,%s,%s'%(self.name,self.age,self.gender,self.college,self.class__)





# 3、创建Teacher类，继承Person类，属性有学院college，专业professional，重写父类personInfo方法，调用父类方法打印个人信息外，将老师的学院、专业信息也打印出来。创建teachObj方法，返回信息为‘今天讲了如何用面向对象设计程序’


class Teacher(Person):
    def __init__(self,college,professional,name,age,gender):
        super(Teacher, self).__init__(name, age, gender)
        self.college = college
        self.professional = professional
    # def __init__(self,*args):
    #     print(args)
    #     super(Teacher, self).__init__(args[2],args[3],args[4])



    def personInfo(self):
        super().personInfo()
        print('专业是{}，学校是{}'.format(self.professional,self.college))

    def teachObj(self):
        return '今天讲了如何用面向对象设计程序'

# 4、创建三个学生对象，分别打印其详细信息
# 5、创建一个老师对象，打印其详细信息
# 6、学生对象调用learn方法
# 7、将三个学员添加至列表中，通过循环将列表中的对象打印出来，print(Student对象)。


if __name__ == '__main__':
    tea = Teacher('北大','汉语言文学','王二',48,'boy')
    tea.personInfo()

    stu = Student('李四',18,'boy','信息技术','计算机科学与技术')
    stu.personInfo()
    stu.study(tea)
    print(Student.__mro__)
    print('##########################################')
    print(stu)