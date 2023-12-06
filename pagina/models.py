from django.db import models

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
    tipo_gasolina = models.CharField(max_length=30, null=True)
    motor =models.CharField(max_length=30, null=True)
    transmision= models.CharField(max_length=20)
    color = models.CharField(max_length=20, null=True)
    cambio_volante = models.BooleanField(null=True)
    tipo_auto = models.CharField(max_length=20, null=True)
    numero_asientos = models.IntegerField(null=True)
    descripcion = models.TextField(max_length=400, null=True)
    auto_delete = models.DateTimeField(null=True)

class Fotos(models.Model):
    path_foto = models.FilePathField()
    auto_id= models.ForeignKey(Autos, on_delete=models.CASCADE)

class Usuarios (models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    sexo = models.IntegerField()
    email = models.CharField(max_length=60) 
    usuario_delete = models.DateTimeField(null=True)

class Contraseñas(models.Model):
    contra= models.CharField(max_length=600)
    contra_delete= models.DateTimeField()
    usuario_id= models.ForeignKey(Usuarios, on_delete=models.CASCADE)

class Notificaciones(models.Model):
    usuario_notificacion_id = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    auto_notificacion_id = models.ForeignKey(Autos,on_delete=models.CASCADE)
    fecha_inicio =models.DateTimeField()
    fecha_final = models.DateTimeField()
    notificaciones_delete = models.DateTimeField()

class Registro(models.Model):
    usuario_registro_id=models.ForeignKey(Usuarios,null=True)
    auto_registro_id= models.ForeignKey(Autos, on_delete=models.CASCADE)
    fecha_registro= models.DateTimeField()
    registro_delete= models.DateTimeField()

