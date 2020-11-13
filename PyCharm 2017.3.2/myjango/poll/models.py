from django.db import models
from django.contrib.auth.models import AbstractUser
from django.views.generic import View

# Create your models here.


class RegisterView(View):
    def get(self,request):
        return