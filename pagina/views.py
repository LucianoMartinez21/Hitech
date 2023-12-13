from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.contrib.auth import authenticate, login
from .forms import Login_Form, Signup_form, Contrasena_form
from .models import Usuarios, Contraseñas
# Create your views here.

def pruebas(resquest):
    return render(resquest,'pruebas.html')

def index(resquest):
    return render(resquest,'index.html')

def detalles_auto(resquest):
    return render(resquest, 'detailcar.html')

def Login(request):
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
            user = authenticate(resquest, email=email, password=password)
            if user is not None:
                login(resquest, user)
                if user.administrador:
                    return redirect('admin-site.html') #placeholder para la pagina donde se ingresara datos y obtendra estadisticas
                else:
                    return redirect('index')
    else:
        form = LoginForm()
    return render(resquest, 'login.html')'''

def signup(resquest):
    if resquest.method == 'GET':
        return render(resquest, 'signup.html', {
            'form' : Signup_form(),
            'form2' : Contrasena_form()
        })
    
    else:
        email = resquest.POST['email']
        
        # Verificar si el usuario ya existe
        if Usuarios.objects.filter(email=email).exists():
            # El usuario ya existe, puedes manejar esto según tus necesidades
            # Puedes mostrar un mensaje de error o redirigir a otra página
            # Aquí simplemente redirigimos a la misma página con un mensaje de error
            return render(resquest, 'signup.html', {
                'form': Signup_form(),
                'form2': Contrasena_form(),
                'error_message': 'Este correo electrónico ya está registrado.'
            })

        # Si el usuario no existe, procedemos a crearlo
        usuario = Usuarios.objects.create(nombre=resquest.POST['nombre'],edad=resquest.POST['edad'],sexo=resquest.POST['sexo'],email=resquest.POST['email'])

        contra = Contraseñas.objects.create(contra=resquest.POST['contrasena'],suario_id=usuario)

        usuario.save()
        contra.save()

        return redirect('index')

def pruebas(request):
    return render(request, 'add-car.html')
