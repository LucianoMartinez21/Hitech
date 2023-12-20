from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Tabla_test(models.Model):
    columna_uno = models.CharField(max_length=200)
    columna_dos = models.CharField(max_length=200)
    columna_tres = models.CharField(max_length=200)
    columna_cuatro = models.CharField(max_length=200)
    numeros = models.IntegerField(default=0)

class Autos(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    ano = models.IntegerField()
    precio = models.IntegerField()
    opciones_combusitble = (
        ('1', '93'),
        ('2', '95'),
        ('3', '97'),
        ('4', 'Petrolero'),
    )
    tipo_gasolina = models.CharField(max_length=1, choices=opciones_combusitble,  null=True)
    opciones_motor = (
        ('1', 'Tipo V'),
        ('2', 'Tipo W'),
        ('3', 'Cilindro opuesto'),
        ('4', 'Electrico'),
    )
    motor =models.CharField(max_length=1, choices=opciones_motor, null=True)
    transmision= models.BooleanField(null=True)
    opciones_color = (
        ('1', 'Rojo'),
        ('2', 'Azul'),
        ('3', 'Verde'),
        ('4', 'Rosa'),
        ('5', 'Blanco'),
        ('6', 'Negro'),
    )
    color = models.CharField(max_length=1, choices=opciones_color, null=True)
    cambio_volante = models.BooleanField(null=True)

    opciones_auto = (
        ('1', 'Sedan'),
        ('2', 'SUV'),
        ('3', 'Deportivo'),
        ('4', 'Hibrido'),
        ('5', 'Electrico'),
        ('6', 'Camion'),
    )
    tipo_auto = models.CharField(max_length=1, choices=opciones_auto, null=True)
    numero_asientos = models.IntegerField(null=True)
    descripcion = models.TextField(max_length=400, null=True)
    auto_delete = models.DateTimeField(null=True)

class Fotos(models.Model):
    path_foto = models.FilePathField()
    auto_id= models.ForeignKey(Autos, on_delete=models.DO_NOTHING)

class Usuarios (AbstractUser):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    opciones_sexo = (
        (1, 'Masculino'),
        (2, 'Femenino'),
        (3, 'Otro'),
    )
    sexo = models.IntegerField(choices=opciones_sexo)
    email = models.EmailField(max_length=255, unique=True)
    administrador= models.BooleanField(default=False)
    usuario_delete = models.DateTimeField(null=True)

    groups = models.ManyToManyField(Group, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios')

class Contraseñas(models.Model):
    contra= models.CharField(max_length=600)
    contra_delete= models.DateTimeField(null=True)
    usuario_id= models.ForeignKey(Usuarios, on_delete=models.CASCADE)

class Notificaciones(models.Model):
    usuario_notificacion_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    auto_notificacion_id = models.ForeignKey(Autos,on_delete=models.CASCADE)
    fecha_inicio =models.DateTimeField()
    fecha_final = models.DateTimeField()

class Registros_visitas(models.Model):
    usuario_registro_id=models.ForeignKey(Usuarios,null=True , on_delete=models.DO_NOTHING)
    auto_registro_id= models.ForeignKey(Autos, on_delete=models.DO_NOTHING)
    fecha_registro= models.DateTimeField()
    registro_delete= models.DateTimeField(null=True)
