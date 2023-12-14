from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Autos
# Create your views here.

def index(request):
    return render(request,'index.html')

def detalles_auto(request):
    return render(request, 'detailcar.html')

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if user.administrador:
                    return redirect('admin-site.html') #placeholder para la pagina donde se ingresara datos y obtendra estadisticas
                else:
                    return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')


def car_list(request):
    cars_list = Autos.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(cars_list, 10) #Muestra 10 autos por pagina

    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1) # si la pagina no es un entero, entrega la primera pagina
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    return render(request, 'car_list.html', {'cars': cars})
