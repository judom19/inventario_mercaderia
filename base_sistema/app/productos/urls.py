from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from app.productos.views import index_productos,Listado_producto,Editar_producto,Borrar_producto,\
Listado_pedido,Editar_pedido,Borrar_producto_pedido,Listado_categorias,inventario_view,Crear_producto,Detalles_producto,Crear_pedido

from django_filters.views import FilterView
from . filters import ProductoFilter
	
#la vista productos_view del archivo views.py

urlpatterns = [
    url(r'^index$', login_required(index_productos), name='index_productos'),#parametros de la url,index sera el
    #segundo patron que buscara django el primer patron a buscar es 'productos '
    #que es el que se encuentra dentro de el archivo de URLS  globales
   	url(r'^nuevo$', login_required(Crear_producto.as_view()), name='productos_nuevo'),
    url(r'^pedido$', login_required(Crear_pedido.as_view()), name='pedido_nuevo'),
   	url(r'^listar$', login_required(Listado_producto.as_view()), name='productos_listar'),
   	url(r'^editar/(?P<pk>\d+)/$', login_required(Editar_producto.as_view()), name='productos_editar'),
	url(r'^productos_detail/(?P<pk>\d+)/$', login_required(Detalles_producto.as_view()), name='productos_detail'),
   	url(r'^buscar_producto$', login_required(FilterView.as_view(filterset_class=ProductoFilter,template_name='producto_filtro_list.html')), name='buscar_producto'),
   	url(r'^eliminar/(?P<pk>\d+)/$', login_required(Borrar_producto.as_view()), name='productos_eliminar'),
   	url(r'^pedido_delete_producto/(?P<pk>\d+)/$', login_required(Borrar_producto_pedido.as_view()), name='pedido_delete_producto'),
   	url(r'^pedido_edit/(?P<pk>\d+)/$', login_required(Editar_pedido.as_view()) , name='pedido_edit'),#debe tener un id
   	#de producto hasta crear los botones en el template
	# url(r'^pedido_filtro$', login_required(FilterView.as_view(filterset_class=ProductoFilter,template_name='producto_id_filtro.html')), name='pedido_filtro'),
   	url(r'^pedido_list$', login_required(Listado_pedido.as_view()), name='pedido_list'),
    url(r'^categorias_list$', login_required(Listado_categorias.as_view()), name='categorias_list'),
    url(r'^inventario_view$', login_required(inventario_view), name='inventario_view'),
	url(r'^buscar_producto_por_empresa$', login_required(FilterView.as_view(filterset_class=ProductoFilter,template_name='stock_por_empresa_filtro_list.html')), name='buscar_producto_por_empresa'),

   	

]	