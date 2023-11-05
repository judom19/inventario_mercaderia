from django.db import models
from perfil.models import EmpresaProveedor

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Factor_empaque(models.Model):
    factor_de_empaque = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.factor_de_empaque

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    marca = models.CharField(max_length=50)
    precio_unitario = models.DecimalField(decimal_places=2, max_digits=10000)
    inventario = models.IntegerField(default=0)
    factor_de_empaque = models.ForeignKey(Factor_empaque, null=True, on_delete=models.SET_NULL)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    empresa_proveedor = models.ForeignKey(EmpresaProveedor, null=True, blank=False, on_delete=models.SET_DEFAULT, default="")
    categoria = models.ManyToManyField(Categoria, blank=True)

    def __str__(self):
        return f'{self.nombre}{self.id}'

class Pedido_mercaderia(models.Model):
    producto_a_pedir = models.OneToOneField(Producto, blank=False, on_delete=models.SET_DEFAULT, default="")
    fecha_compra = models.DateTimeField(auto_now_add=True)
    cantidad = models.IntegerField(blank=False)

    class Meta:
        verbose_name = "Pedido de Producto"
        verbose_name_plural = "Pedidos de Productos"

    def __str__(self):
        return str(self.producto_a_pedir)
