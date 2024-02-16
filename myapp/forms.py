
from django import forms
from .models import Marca, Presentacion,Producto



class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
class PresentacionForm(forms.ModelForm):
    class Meta:
        model = Presentacion
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['marca', 'presentacion', 'precio']
        widgets = {
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'presentacion': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

