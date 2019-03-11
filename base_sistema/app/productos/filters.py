from .models import Producto,Categoria
import django_filters
from django import forms

class ProductoFilter(django_filters.FilterSet):
    	
	categoria = django_filters.ModelMultipleChoiceFilter(queryset=Categoria.objects.all(),widget=forms.CheckboxSelectMultiple)
	nombre = Producto.objects.all().count()

	class Meta:
    		model = Producto
        	fields = [
					
				'empresa_proveedor',
				'categoria',
				'id',
				'nombre',

			]
    