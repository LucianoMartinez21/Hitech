# forms.py
import os
from django import forms
from .models import Usuarios, Autos, Fotos
import datetime
from django.core.files.storage import FileSystemStorage
from multiupload.fields import MultiFileField

class Login_Form(forms.Form):
    email = forms.CharField(label='Email', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Email'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}))



class Signup_form(forms.Form):
    opciones_sexo = (
    (1, 'Masculino'),
    (2, 'Femenino'),
    (3, 'Otro'),
    )
    nombre = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}))
    edad = forms.IntegerField(label='Edad', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Edad'}))
    sexo = forms.ChoiceField(label='Sexo', widget=forms.Select, choices=opciones_sexo)
    email = forms.EmailField(label= 'email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre de Email'}))

class Contrasena_form(forms.Form):
    contrasena= forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}))
    #usuario = forms.ModelChoiceField(queryset=Usuarios.objects.all(), widget=forms.HiddenInput())
'''
class Add_Auto_form(forms.Form):
    marca= forms.CharField(label='Marca', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese marca del auto'}))
    modelo = forms.CharField(label='Modelo', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese modelo del auto'}))
    current_year = datetime.datetime.now().year
    year_choices = [(year, str(year)) for year in range(1950, current_year + 1)]
    ano = forms.ChoiceField(choices=year_choices, label='Seleccione año', widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'año'}))
    precio = forms.IntegerField(label='Precio', widget=forms.IntegerField(attrs={'class': 'form-select', 'placeholder': 'Ingrese el precio del auto'}))
    TIPO_COMBUSTIBLE_CHOICES = [
        ('1', '93'),
        ('2', '95'),
        ('3', '97'),
        ('4', 'Petrolero'),
    ]

    TIPO_MOTOR_CHOICES = [
        ('1', 'Tipo V'),
        ('2', 'Tipo W'),
        ('3', 'Cilindro opuesto'),
        ('4', 'Electrico'),
    ]

    COLOR_CHOICES = [
        ('1', 'Rojo'),
        ('2', 'Azul'),
        ('3', 'Verde'),
        ('4', 'Rosa'),
        ('5', 'Blanco'),
        ('6', 'Negro'),
    ]

    TIPO_AUTO_CHOICES = [
        ('', 'Seleccione el tipo del auto'),
        ('1', 'Sedan'),
        ('2', 'SUV'),
        ('3', 'Deportivo'),
        ('4', 'Hibrido'),
        ('5', 'Electrico'),
        ('6', 'Camion'),
    ]

    tipo_gasolina = forms.ChoiceField(label='Tipo de combustible', choices=TIPO_COMBUSTIBLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el tipo de combustible'}), required=True)
    motor = forms.ChoiceField(label='Tipo de motor',choices=TIPO_MOTOR_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el tipo de motor'}), required=True)
    transmision = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False, label='¿Transmision manual?')
    cambio_volante = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False, label='¿Cambio de volante?')
    color = forms.ChoiceField(label='Color del auto', choices=COLOR_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el color del auto'}), required=True)
    tipo_auto = forms.ChoiceField(label='Tipo del auto',choices=TIPO_AUTO_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el tipo del auto'}), required=True)
    numero_asientos = forms.IntegerField(label='Numero de asientos',widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el numero de asientos'}), required=True)
    descripcion = forms.CharField(label= 'Descripción del auto (maximo de 400 caracteres)', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'maxlength': 400}), required=False)
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'formFileMultiple', 'multiple': True}), required=True)
    image_360_front = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'formFile'}), required=True)
    image_360_rear = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'formFile'}), required=True)

    def save(self, commit=True):
        instance = super(Add_Auto_form, self).save(commit=False)

        # Save photos in a specific location
        photo_path = './pagina/static/img'

        if self.cleaned_data['images']:
            for uploaded_file in self.cleaned_data['images']:
                file_path = os.path.join(photo_path, uploaded_file.name)
                with open(file_path, 'wb') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
            # Create Fotos instance and associate it with Autos
            foto_instance = Fotos.objects.create(path_foto=file_path, auto_id=instance)
            foto_instance.save()

        if self.cleaned_data['image_360_front']:
            file_path = os.path.join(photo_path, self.cleaned_data['image_360_front'].name)
            with open(file_path, 'wb') as destination:
                for chunk in self.cleaned_data['image_360_front'].chunks():
                    destination.write(chunk)
            # Create Fotos instance and associate it with Autos
            foto_instance = Fotos.objects.create(path_foto=file_path, auto_id=instance)
            foto_instance.save()

        if self.cleaned_data['image_360_rear']:
            file_path = os.path.join(photo_path, self.cleaned_data['image_360_rear'].name)
            with open(file_path, 'wb') as destination:
                for chunk in self.cleaned_data['image_360_rear'].chunks():
                    destination.write(chunk)
            # Create Fotos instance and associate it with Autos
            foto_instance = Fotos.objects.create(path_foto=file_path, auto_id=instance)
            foto_instance.save()

        if commit:
            instance.save()
        return instance
'''

"""class Add_Auto_form(forms.Form):
    marca= forms.CharField(label='Marca', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese marca del auto'}))
    modelo = forms.CharField(label='Modelo', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese modelo del auto'}))
    current_year = datetime.datetime.now().year
    year_choices = [(year, str(year)) for year in range(1950, current_year + 1)]
    ano = forms.ChoiceField(choices=year_choices, label='Seleccione año', widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'año'}))
    precio = forms.IntegerField(label='Precio', widget=forms.NumberInput(attrs={'class': 'form-select', 'placeholder': 'Ingrese el precio del auto'}))
    TIPO_COMBUSTIBLE_CHOICES = [
        ('1', '93'),
        ('2', '95'),
        ('3', '97'),
        ('4', 'Petrolero'),
    ]

    TIPO_MOTOR_CHOICES = [
        ('1', 'Tipo V'),
        ('2', 'Tipo W'),
        ('3', 'Cilindro opuesto'),
        ('4', 'Electrico'),
    ]

    COLOR_CHOICES = [
        ('1', 'Rojo'),
        ('2', 'Azul'),
        ('3', 'Verde'),
        ('4', 'Rosa'),
        ('5', 'Blanco'),
        ('6', 'Negro'),
    ]

    TIPO_AUTO_CHOICES = [
        ('', 'Seleccione el tipo del auto'),
        ('1', 'Sedan'),
        ('2', 'SUV'),
        ('3', 'Deportivo'),
        ('4', 'Hibrido'),
        ('5', 'Electrico'),
        ('6', 'Camion'),
    ]

    tipo_gasolina = forms.ChoiceField(label='Tipo de combustible', choices=TIPO_COMBUSTIBLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el tipo de combustible'}), required=True)
    motor = forms.ChoiceField(label='Tipo de motor',choices=TIPO_MOTOR_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el tipo de motor'}), required=True)
    transmision = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False, label='¿Transmision manual?')
    cambio_volante = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False, label='¿Cambio de volante?')
    color = forms.ChoiceField(label='Color del auto', choices=COLOR_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el color del auto'}), required=True)
    tipo_auto = forms.ChoiceField(label='Tipo del auto',choices=TIPO_AUTO_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Seleccione el tipo del auto'}), required=True)
    numero_asientos = forms.IntegerField(label='Numero de asientos',widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el numero de asientos'}), required=True)
    descripcion = forms.CharField(label= 'Descripción del auto (maximo de 400 caracteres)', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'maxlength': 400}), required=False)
    images = MultiFileField(max_file_size=1024 * 1024 * 5, max_num=10, required=False)
    image_360_front = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'formFile'}), required=True)
    image_360_rear = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'formFile'}), required=True)
    print(marca)
    def save(self, commit=True):
        instance = Autos(
            marca=self.cleaned_data['marca'],
            modelo=self.cleaned_data['modelo'],
            ano=self.cleaned_data['ano'],
            precio=self.cleaned_data['precio'],
            tipo_gasolina=self.cleaned_data['tipo_gasolina'],
            motor=self.cleaned_data['motor'],
            transmision=self.cleaned_data['transmision'],
            cambio_volante=self.cleaned_data['cambio_volante'],
            color=self.cleaned_data['color'],
            tipo_auto=self.cleaned_data['tipo_auto'],
            numero_asientos=self.cleaned_data['numero_asientos'],
            descripcion=self.cleaned_data['descripcion']
        )
        print(instance)
        # Save photos in a specific location
        photo_path = '../img'

        if self.cleaned_data['images']:
            for uploaded_file in self.cleaned_data['images']:
                file_path = os.path.join(photo_path, uploaded_file.name)
                with open(file_path, 'wb') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
            # Associate the saved photos with Autos instance
            foto_instance = Fotos.objects.create(path_foto=file_path, auto_id=instance)
            foto_instance.save()

        if self.cleaned_data['image_360_front']:
            file_path = os.path.join(photo_path, self.cleaned_data['image_360_front'].name)
            with open(file_path, 'wb') as destination:
                for chunk in self.cleaned_data['image_360_front'].chunks():
                    destination.write(chunk)
            # Associate the saved photos with Autos instance
            foto_instance = Fotos.objects.create(path_foto=file_path, auto_id=instance)
            foto_instance.save()

        if self.cleaned_data['image_360_rear']:
            file_path = os.path.join(photo_path, self.cleaned_data['image_360_rear'].name)
            with open(file_path, 'wb') as destination:
                for chunk in self.cleaned_data['image_360_rear'].chunks():
                    destination.write(chunk)
            # Associate the saved photos with Autos instance
            foto_instance = Fotos.objects.create(path_foto=file_path, auto_id=instance)
            foto_instance.save()

        if commit:
            instance.save()

        return instance"""



class AutosForm(forms.ModelForm):
    # Especificar los campos que se incluirán en el formulario
    class Meta:
        model = Autos
        fields = ['marca', 'modelo', 'ano', 'precio', 'tipo_gasolina', 'motor', 'transmision', 'color', 'cambio_volante', 'tipo_auto', 'numero_asientos', 'descripcion']




# En el formulario Fotos, asignar el campo path_foto al campo de imagen correspondiente
class FotosForm(forms.ModelForm):
    images = MultiFileField(max_file_size=1024 * 1024 * 5, max_num=20, required=False)
    frontal = forms.ImageField(required=False)
    trasera = forms.ImageField(required=False)

    class Meta:
        model = Fotos
        fields = ['images', 'frontal', 'trasera', 'auto_id']
        widgets = {
            'auto_id': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Indicar que el campo auto_id no es requerido
        self.fields['auto_id'].required = False




class UpdateAutoForm(forms.ModelForm):
    class Meta:
        model = Autos
        fields = ['marca', 'modelo', 'ano', 'precio', 'tipo_gasolina', 'motor', 'transmision', 'color', 'cambio_volante', 'tipo_auto', 'numero_asientos', 'descripcion']