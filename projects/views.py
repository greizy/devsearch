from django.shortcuts import render
from django.http import HttpResponse

# Create your views
def projects(request):
    return HttpResponse('heere our products')


def project(request,pk):
    return HttpResponse('this is single project '+pk)
