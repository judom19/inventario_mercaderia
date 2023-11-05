from .models import Producto, Categoria
import django_filters
from django import forms

class ProductoFilter(django_filters.FilterSet):
    categoria = django_filters.ModelMultipleChoiceFilter(
        queryset=Categoria.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
    class Meta:
        model = Producto
        fields = {
            'empresa_proveedor': ['exact'],
            'categoria': ['exact'],
            'id': ['exact'],
            'nombre': ['exact'],
        }
