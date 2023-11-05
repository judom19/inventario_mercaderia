from django.contrib import admin
from .models import Perfil, EmpresaProveedor

admin.site.register(Perfil, admin.ModelAdmin)
admin.site.register(EmpresaProveedor, admin.ModelAdmin)
