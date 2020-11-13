from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.views import APIView
from celery_tasks.msm import tasks

# Create your views here.

class PhoneCodeView(APIView):

    def get(self,request,phone):
        # 发送短信验证码
        tasks.send_msg_code.delay(phone,'1234',1,2)
        # tasks.send_msg_code(phone,'1234',1,1)

        return HttpResponse(phone)
