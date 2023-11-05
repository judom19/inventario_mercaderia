from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from productos.views import (
    index_productos, Listado_producto, Editar_producto, Borrar_producto,
    Listado_pedido, Editar_pedido, Borrar_producto_pedido, Listado_categorias,
    inventario_view, Crear_producto, Detalles_producto, Crear_pedido, ProductosPorCategoriaView)

from django_filters.views import FilterView
from .filters import ProductoFilter

app_name = 'productos'

urlpatterns = [
    path('index', login_required(index_productos), name='index_productos'),
    path('nuevo', login_required(Crear_producto.as_view()), name='productos_nuevo'),
    path('pedido', login_required(Crear_pedido.as_view()), name='pedido_nuevo'),
    path('listar', login_required(Listado_producto.as_view()), name='productos_listar'),
    re_path(r'^editar/(?P<pk>\d+)/$', login_required(Editar_producto.as_view()), name='productos_editar'),
    re_path(r'^productos_detail/(?P<pk>\d+)/$', login_required(Detalles_producto.as_view()), name='productos_detail'),
    path('buscar_producto', login_required(FilterView.as_view(filterset_class=ProductoFilter, template_name='producto_filtro_list.html')), name='buscar_producto'),
    re_path(r'^eliminar/(?P<pk>\d+)/$', login_required(Borrar_producto.as_view()), name='productos_eliminar'),
    re_path(r'^pedido_delete_producto/(?P<pk>\d+)/$', login_required(Borrar_producto_pedido.as_view()), name='pedido_delete_producto'),
    re_path(r'^pedido_edit/(?P<pk>\d+)/$', login_required(Editar_pedido.as_view()), name='pedido_edit'),
    path('pedido_list', login_required(Listado_pedido.as_view()), name='pedido_list'),
    path('categorias_list', login_required(Listado_categorias.as_view()), name='categorias_list'),
    path('inventario_view', login_required(inventario_view), name='inventario_view'),
    path('buscar_producto_por_empresa', login_required(FilterView.as_view(filterset_class=ProductoFilter, template_name='stock_por_empresa_filtro_list.html')), name='buscar_producto_por_empresa'),
    path('productos/<int:categoria_id>/', ProductosPorCategoriaView.as_view(), name='productos_por_categoria'),


]