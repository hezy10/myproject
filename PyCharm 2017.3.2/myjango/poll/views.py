from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):

    return HttpResponse('Hello Word,You are at the poll index')