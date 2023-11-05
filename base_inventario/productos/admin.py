
from django.contrib import admin
from productos.models import Categoria, Producto, Pedido_mercaderia,Factor_empaque 

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Pedido_mercaderia)
admin.site.register(Factor_empaque)


