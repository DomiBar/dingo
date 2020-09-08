from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def math(request):
    return HttpResponse("Tu będzie matma")


def add(request, a, b):
    return HttpResponse(float(a)+float(b))


def sub(request, a, b):
    return HttpResponse(float(a)-float(b))


def mul(request, a, b):
    return HttpResponse(float(a)*float(b))


def div(request, a, b):
    if b == '0':
        return HttpResponse("Nie dziel przez zero")
    return HttpResponse(float(a)/float(b))
