from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from .forms import PerfilCrear, EmpresaCrear
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import EmpresaProveedor, Perfil


def index_perfiles(request):
    return render(request, 'index_perfil.html')

class RegistroUsuario(CreateView):
    model = User
    template_name = 'CRUD_usuarios.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('perfil:usuario_list')

class Usuario_ListView(ListView):
    model = User
    template_name = 'lista_usuarios.html'

def empresas_index(request):
    return render(request, 'empresas_index.html')

class PerfilCrear(CreateView):
    model = Perfil
    template_name = 'CRUD_Perfiles.html'
    form_class = PerfilCrear
    success_url = reverse_lazy('perfil:proveedores_list')

def proveedores_list(request):
    proveedor = Perfil.objects.all().order_by('id')
    contexto = {'proveedores': proveedor}
    return render(request, 'contactos_proveedores.html', contexto)

class Crear_empresa(SuccessMessageMixin, CreateView):
    model = EmpresaProveedor
    template_name = 'CRUD_empresas.html'
    form_class = EmpresaCrear
    success_url = reverse_lazy('perfil:empresas_list')
    
    def get_success_message(self, cleaned_data):
        return '¡La empresa ha sido registrada con exito!'

class Listado_empresas(ListView):
    model = EmpresaProveedor
    context_object_name = 'empresas'
    ordering = ['id']
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
