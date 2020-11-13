from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import pymysql


from .models import Book,RoleInfo

# Create your views here.
def index(param):
    print('############################')
    print(param)
    return HttpResponse('hello world')

#视图函数注意点
# 1、视图函数必须至少有一个位置参数，用来接受框架传递过来的request对象
# 2、视图函数必须要有一个httpresponse 对象作为返回值


def books(request):
    '''
    实现将所有的书籍信息传递给前端
    :param request: request对象
    :return: response响应
    '''
    # todo 查询所有的书籍信息
    sql = 'select * from book_book'
    data = Book.objects.all()
    print('查询到的书籍信息是',data)
    # todo  构造字典，将字典追加到列表中
    new_list = []
    for item in data:
        new_dict = {'bookname':item.bookname}
        new_list.append(new_dict)

    print('传递给前端的数据',new_list)
    # return HttpResponse(new_list)
    return JsonResponse(new_list,safe=False)



def rolebook(request):
    '''
    # 实现一个功能，根据角色id，返回角色的信息和对应的书籍信息
    :param request:
    :return:
    '''
    # todo 根据id=1，查找出对应的角色
    data = RoleInfo.objects.filter(id=1)[0]
    print(data)

    # todo 构造信息字典
    new_dict = {}
    new_dict['rolename'] = data.rolename
    new_dict['rolegender'] = data.gender

    # todo 查找书籍信息
    print(data.book.bookname)
    new_dict['bookname'] = data.book.bookname


    return JsonResponse(new_dict)

def rolebook(request,param):
    data_list = RoleInfo.objects.filter(id=param)
    if data_list==0:
        return JsonResponse()

def rolebook(request,bookid):
    '''
    用来处理
    :param request:
    :param bookid:
    :return:
    '''
