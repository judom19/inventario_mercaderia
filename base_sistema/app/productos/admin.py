# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.contrib import admin# importando modelos del admin
from app.productos.models import Categoria, Producto, Pedido_mercaderia,Factor_empaque # importando los modelos 
#de productos  

# Registrando modelos para manipularlos desde el admin de django.

admin.site.register(Producto)#registrando modelos

admin.site.register(Categoria)#registrando modelos
admin.site.register(Pedido_mercaderia)
admin.site.register(Factor_empaque)


