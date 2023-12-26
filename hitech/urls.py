"""
URL configuration for hitech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pagina.views import index,sobre_nosotros , eliminar_autos, Login2, detalles_auto, pruebas, signup, addauto, modificar_auto, update_admin,get_admin_status, get_user_details, modificar_admin,notificar_auto, notificacion_admin, notificacion_usuario
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', Login2, name='login'),
    path('signup/', signup,name='signup'),
    path('prueba/', pruebas, name='pruebas'),
    path('modificar_admin/', modificar_admin, name='modificar_admin'),
    path('auto/<int:auto_id>/', detalles_auto, name='detail'),
    path('addcar/', addauto, name='addcar'),
    path('modcar/<int:auto_id>/', modificar_auto, name='modcar'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('update_admin/', update_admin, name='update_admin'),
    path('get_admin_status/<int:user_id>/', get_admin_status, name='get_admin_status'),
    path('get_user_details/<int:user_id>/', get_user_details, name='get_user_details'),
    path('notificar_auto/<int:auto_id>/', notificar_auto, name='notificar_auto'),
    path('notificaciones_admin/', notificacion_admin, name='notificacion_admin'),
    path('notificaciones_usuario/', notificacion_usuario, name='notificacion_usuario'),
    path('sobre_nosotros/', sobre_nosotros, name='sobre_nosotros'),
    path('eliminar_autos/', eliminar_autos , name='eliminar_autos'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)