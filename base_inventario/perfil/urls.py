from django.urls import path
from .views import RegistroUsuario, empresas_index, Usuario_ListView, proveedores_list, Listado_empresas, Crear_empresa, Editar_empresa, Eliminar_empresa, PerfilCrear, index_perfiles
from django.contrib.auth.decorators import login_required

app_name = 'perfil'
urlpatterns = [
    path('index_perfiles/', index_perfiles, name='index_perfiles'),
    path('crear', login_required(RegistroUsuario.as_view()), name='crear'),
    path('usuario_list', Usuario_ListView.as_view(), name='usuario_list'),
    path('empresas_index', empresas_index, name='empresas_index'),
    path('empresa', Crear_empresa.as_view(), name='empresa'),
    path('empresas_list', Listado_empresas.as_view(), name='empresas_list'),
    path('editar/<int:pk>/', Editar_empresa.as_view(), name='empresas_edit'),
    path('eliminar/<int:pk>/', Eliminar_empresa.as_view(), name='empresas_delete'),
    path('proveedores_crear', PerfilCrear.as_view(), name='proveedores_crear'),
    path('proveedores_list', proveedores_list, name='proveedores_list'),
]
