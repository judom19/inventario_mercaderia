# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from app.productos.forms import ProductoForm,Pedido_mercaderiaForm #importando el formulario 
from app.productos.models import Producto,Pedido_mercaderia, Categoria#importando modelo Producto
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import ProductoFilter





#Vistas APP PRODUCTO
def index_productos(request):#con request  se le indica que reciba la peticion
	return render(request, 'index_productos.html')
   

def inventario_view(request):
    return render(request, 'index_inventario.html')

class Listado_producto(ListView):
	ordering = ['empresa_proveedor']   
	model = Producto
	template_name = 'lista_productos.html'
	paginate_by = 6

  
class Crear_producto(SuccessMessageMixin,CreateView):
    model = Producto
    template_name = 'productos_form.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:productos_listar')
    def get_success_message(self,cleaned_data):
        print cleaned_data
        return 'Datos guardados'

class Editar_producto(UpdateView):
    model = Producto
    template_name = 'productos_form.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:productos_listar')
class Borrar_producto(DeleteView):
    model = Producto
    template_name = 'productos_delete.html'
    success_url =reverse_lazy('productos:productos_listar')

class Detalles_producto(DetailView):
    model = Producto
    queryset = Producto.objects.all()#ordenando
    template_name = 'detalles_productos.html'
#Creando vista para hacer pedidos

class Crear_pedido(CreateView):
	model = Pedido_mercaderia
	template_name = 'CRUD_pedido.html'
	form_class = Pedido_mercaderiaForm
	success_url = reverse_lazy('productos:pedido_list')
class Editar_pedido(UpdateView):
    model = Pedido_mercaderia
    template_name = 'CRUD_pedido.html'
    form_class = Pedido_mercaderiaForm
    success_url = reverse_lazy('productos:pedido_list')


class Listado_pedido(ListView):
    ordering = ['id']   
    model = Pedido_mercaderia
    # queryset= Pedido_mercaderia.objects.filter()
    template_name = 'pedido_reporte.html'
  

class Borrar_producto_pedido(DeleteView):
    model = Pedido_mercaderia
    template_name = 'producto_pedido_delete.html'
    success_url =reverse_lazy('productos:pedido_list')

class Listado_categorias(ListView):
    	
    ordering = ['id']   
    model = Categoria
    template_name = 'lista_categorias.html'



# def search(request):
#     producto_list = Producto.objects.all()
#     producto_filter = ProductoFilter(request.GET, queryset=producto_list)
#     return render(request, 'CRUD_pedido.html', {'filter': producto_filter})