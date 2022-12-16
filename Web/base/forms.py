from django import forms
from .models import Venta

class VentasForm(forms.ModelForm):
    class Meta:
        model= Venta
        fields= '__all__'