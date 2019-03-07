from django.conf.urls import url
from .views import RegistroUsuario,index_perfils,empresas_index, \
Usuario_ListView,proveedores_list,Listado_empresas,Crear_empresa,Editar_empresa,Eliminar_empresa,PerfilCrear
from django.contrib.auth.decorators import login_required

urlpatterns = [
	url(r'^index$', login_required(index_perfils), name='index'),
    url(r'^crear$', login_required(RegistroUsuario.as_view()), name='crear'),  # pasando los parametros de la url,index sera el
    # segundo patron que buscara django el primer patron a buscar es 'productos '
    # que es el que se encuentra dentro de el archivo de URLS  globales
    url(r'^usuario_list$', Usuario_ListView.as_view(), name='usuario_list'),
    url(r'^empresas_index$', empresas_index, name='empresas_index'),
    url(r'^empresa$', Crear_empresa.as_view(), name='empresa'),
    url(r'^empresas_list$', Listado_empresas.as_view(), name='empresas_list'),
    url(r'^editar/(?P<pk>\d+)/$',Editar_empresa.as_view(),name='empresas_edit'),
    url(r'^eliminar/(?P<pk>\d+)/$', Eliminar_empresa.as_view(), name='empresas_delete'),
    ##proveedores
    url(r'^proveedores_crear$', PerfilCrear.as_view(), name='proveedores_crear'),
    url(r'^proveedores_list$', proveedores_list, name='proveedores_list'),
   


]