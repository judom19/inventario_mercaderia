from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from productos.forms import ProductoForm, Pedido_mercaderiaForm
from productos.models import Producto, Pedido_mercaderia, Categoria
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import ProductoFilter
from django_filters.views import FilterView

def index_productos(request):
    return render(request, 'index_productos.html')

def inventario_view(request):
    return render(request, 'index_inventario.html')

class Listado_producto(ListView):
    ordering = ['empresa_proveedor']
    model = Producto
    template_name = 'lista_productos.html'
    paginate_by = 6

class Crear_producto(SuccessMessageMixin, CreateView):
    model = Producto
    template_name = 'productos_form.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:productos_listar')
    success_message = "Articulo almacenado correctamente"

class Editar_producto(UpdateView):
    model = Producto
    template_name = 'productos_form.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:productos_listar')

class Borrar_producto(DeleteView):
    model = Producto
    template_name = 'productos_delete.html'
    success_url = reverse_lazy('productos:productos_listar')

class Detalles_producto(DetailView):
    model = Producto
    queryset = Producto.objects.all()
    template_name = 'detalles_productos.html'

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
    template_name = 'pedido_reporte.html'

class Borrar_producto_pedido(DeleteView):
    model = Pedido_mercaderia
    template_name = 'producto_pedido_delete.html'
    success_url = reverse_lazy('productos:pedido_list')


class Listado_categorias(ListView):
    model = Categoria
    template_name = 'lista_categorias.html'
    context_object_name = 'categorias'

    def get_queryset(self):
        # Obtener la lista de categorías con la cantidad de artículos por categoría
        from django.db.models import Count
        return Categoria.objects.annotate(num_articulos=Count('producto'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener la lista de categorías con la cantidad de artículos por categoría
        context['categorias'] = self.get_queryset()
        return context

class ProductosPorCategoriaView(ListView):
    model = Producto
    template_name = 'productos_por_categoria.html'
    context_object_name = 'productos'

    def get_queryset(self):
        categoria_id = self.kwargs['categoria_id']
        return Producto.objects.filter(categoria__id=categoria_id)

class ProductoFilterView(FilterView):
    filterset_class = ProductoFilter
    template_name = 'producto_filtro_list.html'
    queryset = Producto.objects.all()
