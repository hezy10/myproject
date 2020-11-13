"""
面向对象
将数据和函数一起封装，减少了重复代码

面向过程
根据业务逻辑从上到下依次写代码
"""


# 类和对象
# 类：创建实例对象的模板，具有相同属性和行为动作的统称
class EatClass(object):

    def opendoor(self):
        '''
        开门
        :return:
        '''
        print('上完课，打开门')

    def waitlift(self, time):
        '''
        等电梯
        :param time: 等待时间
        :return:
        '''
        print('正在等电梯',time)

    def cross_the_road(self,time):
        '''
        过马路
        :param time: 过马路需要时间
        :return:
        '''
        print('穿过马路',time)

    def rice(self,money,kind):
        '''
        买饭
        :param money: 金额
        :param kind: 菜的种类
        :return:
        '''
        print('菜品等种类',kind,'饭菜的金额',money)

    def eat(self):
        '''
        吃饭
        :return:
        '''
        print('买完饭回来吃')