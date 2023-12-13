# forms.py
from django import forms
from .models import Usuarios

class Login_Form(forms.Form):
    email = forms.CharField(label='Email', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Email'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}))

class Signup_form(forms.Form):
    nombre = forms.CharField(label='Nombre de usuario', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre de usuario'}))
    edad = forms.IntegerField(label='Edad', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Edad'}))
    sexo = forms.IntegerField(label='Sexo', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su Sexo'}))
    email = forms.EmailField(label= 'email', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre de Email'}))

class Contrasena_form(forms.Form):
    contrasena= forms.CharField(label='Contraseña', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su contraseña'}))
    #usuario = forms.ModelChoiceField(queryset=Usuarios.objects.all(), widget=forms.HiddenInput())
