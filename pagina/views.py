from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import Login_Form, Signup_form, Contrasena_form, AutosForm, FotosForm
from .models import Usuarios, Contrasenas, Autos, Fotos
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import AbstractUser
from django.forms import formset_factory
import os
# Create your views here.

def pruebas(request):
    return render(request,'pruebas.html')

def index(request):
    autos_list = Autos.objects.all()
    # Fetch all images for each auto
    autos_with_images = []
    for auto in autos_list:
        images = Fotos.objects.filter(auto_id=auto)
        #if images:
        #    print(images.first().path_foto.url)
        #else:
        #    print("No images found for auto:", auto.id)
        autos_with_images.append({'auto': auto, 'images': images})
    paginator = Paginator(autos_list, 2)  # Set the number of autos per page


    page = request.GET.get('page')
    try:
        autos = paginator.page(page)
    except PageNotAnInteger:
        autos = paginator.page(1)
    except EmptyPage:
        autos = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'autos': autos})

def addauto(request):
    if request.method == 'POST':
        autos_form = AutosForm(request.POST)
        fotos_form = FotosForm(request.POST, request.FILES)

        if autos_form.is_valid() and fotos_form.is_valid():
            auto = autos_form.save()

            # Ruta al directorio donde se guardarán las fotos
            directorio_fotos = 'img'  # Reemplaza con la ruta real

            # Verifica si el directorio existe y créalo si no
            if not os.path.exists(directorio_fotos):
                os.makedirs(directorio_fotos)

            # Iterar sobre cada foto que se sube en el campo images
            for foto in request.FILES.getlist('images'):
                fotos = Fotos(auto_id=auto)
                fotos.path_foto.save(f'{directorio_fotos}id:{auto}_{foto.name}', foto)

            # Repetir el mismo proceso para las fotos frontal y trasera
            for field_name in ['frontal', 'trasera']:
                foto = request.FILES.get(field_name)
                if foto:
                    fotos = Fotos(auto_id=auto)
                    fotos.path_foto.save(f'360img_id:{auto}_{foto.name}', foto)


            return redirect('index') #hacer que se conecte con detailcar
    else:
        autos_form = AutosForm()
        fotos_form = FotosForm()
    return render(request, 'add-car.html', {'autos_form': autos_form, 'fotos_form': fotos_form})

def detalles_auto(request, auto_id):
    auto = get_object_or_404(Autos, pk=auto_id)
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
                contrasena = Contrasenas.objects.get(usuario_id=usuario.id, contra=password)

                # Si la consulta tiene éxito, los datos son correctos
                # Puedes realizar otras acciones, como iniciar sesión, redireccionar, etc.
                #login(request, usuario)
                user = authenticate(request, email=email, password=password)
                if user is not None:
                # Login the user
                    login(request, user)
                    print("bienvenido")
                    print(user.administrador)
                    return redirect('index')
                #print(usuario.administrador)
                #print(login(request, usuario))
               # return redirect('index')

            except (Usuarios.DoesNotExist, Contrasenas.DoesNotExist):
                # Si no se encuentra el usuario o la contraseña no coincide, puedes mostrar un mensaje de error
                form.add_error(None, "Email o contraseña incorrectos")

    else:
        form = Login_Form()

    return render(request, 'login.html', {'form': form})

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

        contra = Contrasenas.objects.create(contra=request.POST['contrasena'],usuario_id=usuario)

        usuario.save()
        contra.save()
        #login(request, usuario)
        return redirect('index')

def pruebas(request):
    return render(request, 'add-car.html')
