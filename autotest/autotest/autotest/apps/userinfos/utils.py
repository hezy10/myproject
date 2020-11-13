import re


from . import models



def jwt_response_payload_handler(token, user=None, request=None):
    print('########################################')
    print(user)
    return {
        'token': token,
        'username':user.username,
        'user_id':user.id,
        'phone':user.phone

    }



class MyAuthLoginBackends:
    def authenticate(self, request, username=None, password=None, **kwargs):
        '''

        :param request:
        :param username: 前端传递的数据可能是用户名,也有可能是手机号码,也有可能是邮箱
        :param password:
        :param kwargs:
        :return:
        '''
        print('##########进入重写的登陆方法###############')

        # todo 判断username到时是什么数据类型
        try:
            if re.match('^1[3,5,7,8,6]\d{9}$',username):
                user = models.User.objects.get(phone=username)
                print('通过手机号码获取用户')
            elif re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$',username):
                user = models.User.objects.get(email=username)
            else:
                user = models.User.objects.get(username=username)
        except Exception as e:
            user = None

        if user is not None and user.check_password(password):
            return user




        print(username)
        print(type(username))
        # return user
