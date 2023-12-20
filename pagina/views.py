from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from .forms import Login_Form, Signup_form, Contrasena_form
from .models import Usuarios, Contraseñas
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Autos
from django.contrib.auth.models import AbstractUser
# Create your views here.

def pruebas(request):
    return render(request,'pruebas.html')

def index(request):
    return render(request,'index.html')

def detalles_auto(request, auto_id):
    auto = Autos.objects.get(pk=auto_id)
    return render(request, 'detailcar.html', {'auto' : auto})

def Login2(request):
    if request.method == 'POST':
        form = Login_Form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Verificar si el email y la contraseña coinciden en las tablas Usuarios y Contraseñas
            try:
                usuario = Usuarios.objects.get(email=email)
                contrasena = Contraseñas.objects.get(usuario_id=usuario.id, contra=password)

                # Si la consulta tiene éxito, los datos son correctos
                # Puedes realizar otras acciones, como iniciar sesión, redireccionar, etc.
                return redirect('index')

            except (Usuarios.DoesNotExist, Contraseñas.DoesNotExist):
                # Si no se encuentra el usuario o la contraseña no coincide, puedes mostrar un mensaje de error
                form.add_error(None, "Email o contraseña incorrectos")

    else:
        form = Login_Form()

    return render(request, 'login.html', {'form': form})

    '''if resquest.method == 'POST':
        form = LoginForm(resquest.POST)
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
    return render(resquest, 'login.html')'''

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form' : Signup_form(),
            'form2' : Contrasena_form()
        })

    else:
        email = request.POST['email']

        # Verificar si el usuario ya existe
        if Usuarios.objects.filter(email=email).exists():
            # El usuario ya existe, puedes manejar esto según tus necesidades
            # Puedes mostrar un mensaje de error o redirigir a otra página
            # Aquí simplemente redirigimos a la misma página con un mensaje de error
            return render(request, 'signup.html', {
                'form': Signup_form(),
                'form2': Contrasena_form(),
                'error_message': 'Este correo electrónico ya está registrado.'
            })

        # Si el usuario no existe, procedemos a crearlo
        usuario = Usuarios.objects.create(nombre=request.POST['nombre'],edad=request.POST['edad'],sexo=request.POST['sexo'],email=request.POST['email'], username = request.POST['nombre'])

        contra = Contraseñas.objects.create(contra=request.POST['contrasena'],usuario_id=usuario)

        usuario.save()
        contra.save()
        login(request, usuario)
        return redirect('index')

def pruebas(request):
    return render(request, 'add-car.html')
'''
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

    return render(request, 'index.html', {'cars': cars})
'''
