# # def func1():
# #     print('这是函数func1')
# #
# #
# # if __name__ == '__main__':
# #     func1()
# #     func2 = func1
# #     print(id(func1))
# #     print(id(func2))
# #     func2()
# #     # print(id(1999999))
# #     # print(id(1999999))
# #     # print(id(1999999))
#
#
# # def wrapper(num1):
# #     def inner(num2):
# #         print(num1,num2)
# #
# #     return inner
#
#
def linner(k,b):

    def inner(x):

        print(k*x+b)

    return inner


if __name__ == '__main__':
    # LEGB
    func = linner(1,1)
    func(1)
#     # func = wrapper(1)
#     # func(2)
#     # print(func)
#
#
#
#

# def checkpwd():
#     pass
#
#
# def checkauth():
#     pass
#
# def wrapper(func):
#     def inner():
#         # 第一验证  验证是否登录
#         # 第二验证  验证是否具有权限
#         # print(func)
#         func()
#     return inner
#
# @wrapper
# def ordering():
#     # 第一验证  验证是否登录
#     # 第二验证  验证是否具有权限
#     # checkpwd()
#     # checkauth()
#
#     print('------正在下订单-------------')
#
# @wrapper
# def changepwd():
#     # 第一验证  验证是否登录
#     # 第二验证  验证是否具有权限
#     # checkpwd()
#     # checkauth()
#
#     print('-----------修改密码----------')
#
#
# def showinfo():
#     # 第一验证  验证是否登录
#     # 第二验证  验证是否具有权限
#     # checkpwd()
#     # checkauth()
#
#     print('---------个人信息------------')
#
#
# if __name__ == '__main__':
#     # func = wrapper(changepwd)
#     # func()
#     ordering()
#     changepwd()
#     showinfo()