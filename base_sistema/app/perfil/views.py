# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from .forms import PerfilCrear, UsuarioCrear,EmpresaCrear
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import EmpresaProveedor,Perfil



# Create your views here.



# Create your views here.
def index_perfils(request):
    return render(request,'index_perfil.html')

class RegistroUsuario(CreateView):
    model= User
    template_name = 'CRUD_usuarios.html'
    form_class = UserCreationForm
    success_url =reverse_lazy('perfil:usuario_list')
        
class Usuario_ListView(ListView):#recibe la peticion request
    #Creando Queryset con nombre producto
    #el modelo Producto y lo meto en la variable producto
    model = User
    template_name = 'lista_usuarios.html'




def empresas_index(request):
    return render(request,'empresas_index.html')

class PerfilCrear(CreateView):
    model= Perfil
    template_name = 'CRUD_Perfiles.html'
    form_class = PerfilCrear
    success_url =reverse_lazy('perfil:proveedores_list')

def proveedores_list(request):
    proveedor = Perfil.objects.all().order_by('id')
    contexto = {'proveedores':proveedor}
    return render(request, 'contactos_proveedores.html', contexto)

####### PASADO TODAS LAS VISTA DE VISTAS DE FUNCIONES A CLASES
   
class Crear_empresa(SuccessMessageMixin,CreateView):
    model = EmpresaProveedor
    template_name = 'CRUD_empresas.html'
    form_class = EmpresaCrear
    success_url = reverse_lazy('perfil:empresas_list')
    def get_success_message(self,cleaned_data):
        print cleaned_data
        return 'Datos guardados'




class Listado_empresas(ListView):
    ordering = ['id']   
    model = EmpresaProveedor
    context_object_name = 'empresas'
    paginate_by = 6
    template_name = 'listado_empresas.html'
    
 

class Editar_empresa(UpdateView):
    model = EmpresaProveedor
    template_name = 'CRUD_empresas.html'
    form_class = EmpresaCrear
    success_url = reverse_lazy('perfil:empresas_list')

class Eliminar_empresa(DeleteView):
    model = EmpresaProveedor
    template_name = 'empresa_delete.html'
    success_url = reverse_lazy('perfil:empresas_list')
