from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hope page')

def about(request):
    return HttpResponse('About page')