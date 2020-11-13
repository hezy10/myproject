from django.http.response import HttpResponse
from rest_framework.generics import CreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView
from rest_framework.response import Response
from django.db import DatabaseError
from rest_framework.permissions import IsAuthenticated


from .serializers import UserSerilizer,UserInfoSerializer
from .models import User




class RegisterView(CreateAPIView):
    serializer_class = UserSerilizer
    queryset = User.objects.all()

    # def get(self,response):
    #     # raise DatabaseError('数据库异常')
    #     return Response('ok')


class UserinfoView(RetrieveUpdateAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user



# /usr/local/bin/virtualenvwrapper.sh
# Xiaxingxing123



# class ChangeUserView()