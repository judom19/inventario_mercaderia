from django import forms
from productos.models import Producto, Pedido_mercaderia

class ProductoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control col-md-12'}))
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'descripcion',
            'marca',
            'precio_unitario',
            'inventario',
            'factor_de_empaque',
            'empresa_proveedor',
            'categoria',
        ]
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'marca': 'Marca',
            'precio_unitario': 'Precio/unidad',
            'factor_de_empaque': 'Factor de empaque',
            'inventario': 'Inventario',
            'empresa_proveedor': 'Proveedor',
            'categoria': 'Categoría',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-group'}),
            'descripcion': forms.Textarea(attrs={'cols': 56, 'rows': 5}),
            'marca': forms.TextInput(attrs={'class': 'form-group'}),
            'precio_unitario': forms.TextInput(attrs={'class': 'form-group'}),
            'factor_de_empaque': forms.Select(attrs={'class': 'form-group'}),
            'inventario': forms.TextInput(attrs={'class': 'form-group'}),
            'empresa_proveedor': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'}),
        }

class Pedido_mercaderiaForm(forms.ModelForm):
    class Meta:
        model = Pedido_mercaderia
        fields = ['producto_a_pedir', 'cantidad']
        labels = {
            'producto_a_pedir': 'Elegir Mercadería',
            'cantidad': '¿Cuántos artículos desea pedir?',
        }
        widgets = {
            'producto_a_pedir': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
        }
