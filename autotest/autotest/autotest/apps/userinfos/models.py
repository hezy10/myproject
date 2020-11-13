from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    GENDER = (
        ('male','男'),
        ('female','女'),
        ('secret','保密'),
    )
    gender = models.CharField(max_length=32,choices=GENDER,default='男',verbose_name='性别')
    phone = models.CharField(max_length=11,verbose_name='手机号码')
    c_time = models.DateTimeField(auto_now_add=True,verbose_name='注册时间')
    isDelete = models.BooleanField(default=False)


    class Meta:
        db_table = 'at_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     '''将模型的实例对象以字符串的形式输出'''
    #     return self.username