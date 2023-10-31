from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola(resquest):
    return HttpResponse("hola mundo")