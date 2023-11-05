from django import forms
from .models import Perfil, EmpresaProveedor
from django.contrib.auth.models import User


class PerfilCrear(forms.ModelForm):
    direccion = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 24}))

    class Meta:
        model = Perfil
        fields = ('empresa_proveedor', 'usuario', 'direccion', 'telefono', 'dui', 'nit')
        labels = {
            'usuario': 'Usuario',
            'empresa_proveedor': 'Empresa',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'dui': 'DUI',
            'nit': 'NIT',
        }


class UsuarioCrear(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')
        labels = {
            'username': 'Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'password': 'Contraseña',
        }

class EmpresaCrear(forms.ModelForm):
    class Meta:
        model = EmpresaProveedor
        fields = ('nombre_empresa', 'nit', 'telefono', 'contacto_email')
        labels = {
            'nombre_empresa': 'Nombre de la Empresa',
            'nit': 'NIT',
            'telefono': 'Teléfono',
            'contacto_email': 'Correo Electrónico',
        }
