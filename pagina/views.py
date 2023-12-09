from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *
# Create your views here.

def index(resquest):
    return render(resquest,'index.html')

def detalles_auto(resquest):
    return render(resquest, 'detailcar.html')

def Login(resquest):
    if resquest.method == 'POST':
        form = LoginForm(resquest.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(resquest, email=email, password=password)
            if user is not None:
                login(resquest, user)
                if user.administrador:
                    return redirect('admin-site.html') #placeholder para la pagina donde se ingresara datos y obtendra estadisticas
                else:
                    return redirect('index')
    else:
        form = LoginForm()
    return render(resquest, 'login.html')

def signup(resquest):
    return render(resquest, 'signup.html')
