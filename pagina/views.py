from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import Login_Form, Signup_form, Contrasena_form, AutosForm, FotosForm, UpdateAutoForm
from .models import Usuarios, Contrasenas, Autos, Fotos, Notificaciones
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import AbstractUser
from django.forms import formset_factory
import os
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.

def es_admin(user):
    return user.is_authenticated and user.administrador

def pruebas(request):
    return render(request,'pruebas.html')

def index(request):
    autos_list = Autos.objects.all()
    # Fetch all images for each auto
    autos_with_images = []
    for auto in autos_list:
        images = Fotos.objects.filter(auto_id=auto)
        autos_with_images.append({'auto': auto, 'images': images})
    paginator = Paginator(autos_with_images, 2)  # Set the number of autos per page

    page = request.GET.get('page')
    try:
        autos = paginator.page(page)
    except PageNotAnInteger:
        autos = paginator.page(1)
    except EmptyPage:
        autos = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'autos': autos})

@user_passes_test(es_admin, login_url='index')
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

@user_passes_test(es_admin, login_url='index')
def modificar_auto(request, auto_id):
    auto = get_object_or_404(Autos, pk = auto_id)
    if request.method == 'POST':
        form = UpdateAutoForm(request.POST, instance = auto)
        if form.is_valid():
            form.save()
            return redirect('detail', auto_id = auto.pk)
    else:
        form = UpdateAutoForm(instance=auto)
    return render(request, 'mod-car.html', {'form': form, 'auto': auto})


def detalles_auto(request, auto_id):
    auto = get_object_or_404(Autos, pk=auto_id)
    images = Fotos.objects.filter(auto_id=auto.pk).exclude(path_foto__startswith='360img_id')
    images360 = Fotos.objects.filter(auto_id=auto.pk, path_foto__startswith='360img_id')
    context = {
        'auto': auto,
        'images': images,
        'images_360': images360,
    }
    return render(request, 'detailcar.html', context)

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

@user_passes_test(es_admin, login_url='index')
def modificar_admin(request):
    usuarios = Usuarios.objects.all()
    administrador_actual = Usuarios.objects.first().administrador  # O el valor que prefieras
    return render(request, 'modificar_admin.html', {'usuarios': usuarios})

def update_admin(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_select')
        admin_checkbox = request.POST.get('admin_checkbox')
        
        usuario = Usuarios.objects.get(id=user_id)
        usuario.administrador = admin_checkbox is not None
        usuario.save()

    return redirect('pruebas')

def get_admin_status(request, user_id):
    usuario = Usuarios.objects.get(id=user_id)
    data = {'administrador': usuario.administrador}
    return JsonResponse(data)

def get_user_details(request, user_id):
    usuario = Usuarios.objects.get(id=user_id)
    data = {
        'nombre': usuario.nombre,
        'edad': usuario.edad,
        'sexo': usuario.get_sexo_display(),  # Obtiene el valor desplegable en lugar del código
        'email': usuario.email,
        'administrador': usuario.administrador,
    }
    return JsonResponse(data)

def notificar_auto(request, auto_id):
    if request.user.is_authenticated:
        auto = get_object_or_404(Autos, pk=auto_id)

        # Verifica si el usuario ya tiene una notificación para este auto
        existe_notificacion = Notificaciones.objects.filter(
            usuario_notificacion_id=request.user,
            auto_notificacion_id=auto
        ).exists()

        if not existe_notificacion:
            # Crea una nueva notificación con fecha de inicio actual y fecha final un día después
            fecha_inicio = timezone.now()
            fecha_final = fecha_inicio + timedelta(days=1)
            
            Notificaciones.objects.create(
                usuario_notificacion_id=request.user,
                auto_notificacion_id=auto,
                fecha_inicio=fecha_inicio,
                fecha_final=fecha_final
            )
            messages.success(request, f'¡Te notificaremos cuando haya novedades sobre el auto {auto.modelo}!')
        else:
            messages.warning(request, f'Ya estás notificado sobre el auto {auto.modelo}.')

    else:
        messages.error(request, 'Debes iniciar sesión para notificar sobre un auto.')

    return redirect('detail', auto_id=auto_id)


def notificacion_admin(request):
    # Obtén la lista de autos con al menos una notificación
    autos_con_notificaciones = Autos.objects.annotate(num_notificaciones=Count('notificaciones')).filter(num_notificaciones__gt=0)

    context = {
        'autos_con_notificaciones': autos_con_notificaciones,
    }

    if request.method == 'POST':
        auto_id = request.POST.get('auto_id')  # Obtén el ID del auto desde el formulario
        auto = get_object_or_404(Autos, pk=auto_id)
        
        # Envia el correo electrónico a los usuarios vinculados al auto
        enviar_correo_notificacion(auto)

        messages.success(request, f'Correo electrónico de notificación enviado para el auto {auto.modelo}.')

    return render(request, 'notificacion_admin.html', context)

def enviar_correo_notificacion(auto):
    usuarios_auto = Usuarios.objects.filter(notificaciones__auto_notificacion_id=auto)
    asunto = 'Notificación sobre un auto'
    mensaje = f'Hola,\n\nSe ha actualizado información sobre el auto {auto.marca} {auto.modelo}. Visita el sitio para obtener más detalles.'

    for usuario in usuarios_auto:
        send_mail(asunto, mensaje, 'marcos_challapa@yahoo.com', [usuario.email])

def notificacion_usuario(request):
    if request.method == 'POST':
        auto_id = request.POST.get('auto_id')
        if auto_id:
            Notificaciones.objects.filter(usuario_notificacion_id=request.user, auto_notificacion_id=auto_id).delete()
            return redirect('notificacion_usuario')

    notificaciones_usuario = Notificaciones.objects.filter(usuario_notificacion_id=request.user)
    autos_notificados = [notificacion.auto_notificacion_id for notificacion in notificaciones_usuario]

    context = {
        'autos_notificados': autos_notificados,
    }

    return render(request, 'notificacion_usuario.html', context)


def pruebas(request):
    return redirect("index")

