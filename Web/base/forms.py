from django import forms
from .models import Venta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VentasForm(forms.ModelForm):
    class Meta:
        model= Venta
        fields= '__all__'

class RegistroUsuario(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']