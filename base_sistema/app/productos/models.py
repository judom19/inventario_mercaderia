# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.db import models


from app.perfil.models import EmpresaProveedor

#poner dos forek uno a productos y otro a categorias
class Categoria(models.Model):
	"""docstring for Tipo_producto"""
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return '{}'.format(self.nombre)
class Factor_empaque(models.Model):
	"""docstring for Tipo_producto"""
	factor_de_empaque = models.CharField(max_length=30,blank=False)

	def __unicode__(self):
		return '{}'.format(self.factor_de_empaque)


#forek hacia categorias
class Producto(models.Model):
	#creando atributos
	nombre = models.CharField(max_length = 50)#el tipo de campo charfield recibe de
	#parametro por obligacion la propiedad o argumento max_length
	descripcion = models.TextField(blank=True, null=True)#texto plano
	marca = models.CharField(max_length=50)
	precio_unitario = models.DecimalField(decimal_places=2, max_digits=10000)
	inventario=models.IntegerField( default=0)
	factor_de_empaque = models.ForeignKey(Factor_empaque, null=True)
	fecha_compra = models.DateTimeField(auto_now_add=True,)
	empresa_proveedor = models.ForeignKey(EmpresaProveedor, null=True, blank= False)#relacion de uno a muchos
	#un proveedor puede tener muchos productos
	#o muchos productos pueden pertenecer a un mismo proveredor
	categoria = models.ManyToManyField(Categoria, blank=True)#relacion de muchos a muchos
	#muchos productos puede pertenecer de uno o mas categorias
	

	def __unicode__(self):#funcion para que se nos devuelva el nombre y no el objeto
	#que hemos registrado
		return '{}{}'.format(self.nombre,self.id)#en este caso la llave foranea del proveedor
		#y que nos muestre en un select el nombre de la empresa
		#creando modelo para realizar un pedido

class Pedido_mercaderia(models.Model):# mas adelante agregare un numero de pedido, el id del producto
# y fecha en que se realiza el pedido
	producto_a_pedir = models.OneToOneField(Producto, blank=False)
	fecha_compra= models.DateTimeField(auto_now_add=True,)
	cantidad = models.IntegerField(blank= False)


	class Meta:
		verbose_name = "Pedido_Producto"
		verbose_name_plural = "Pedido_Productos"
	def __unicode__(self):#
		return '{}'.format(self.producto_a_pedir)#
