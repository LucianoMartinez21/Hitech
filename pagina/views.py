from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(resquest):
    return render(resquest,'index.html')

def detalles_auto(resquest):
    return render(resquest, 'detailcar.html')

def login(resquest):
    return render(resquest, 'login.html')

def signup(resquest):
    return render(resquest, 'signup.html')