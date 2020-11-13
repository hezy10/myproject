from rest_framework.views import exception_handler
from django.db import DatabaseError
from redis.exceptions import RedisError
from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR

def custom_exception_handler(exc, context):
    '''

    :param exc: 异常对象 例如:<class 'rest_framework.exceptions.MethodNotAllowed'>
    :param context: 抛出异常的上下文
    :return:
    '''
    print('现在进行自定义异常')
    # print('exc',exc)
    # print(type(exc))
    print(context)
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # 自带的restframework 异常可以被处理,还有可以姐姐django的404和权限
    # 其他的异常不能被处理,返回的数据是None,但是我们可以自己实现
    # restframework处理不了的异常
    if response is None:
        # todo 判断异常所属的类
        if isinstance(exc,DatabaseError) or isinstance(exc,RedisError):
            print('------------------->',exc)
            response = Response({'msg':'服务器内部数据库问题'},status=HTTP_500_INTERNAL_SERVER_ERROR)



    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response