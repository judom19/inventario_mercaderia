# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import Permission, User
#from app.productos.models import Categoria
# Create your models here.
#poner dos forek uno a productos y otro a categorias
class EmpresaProveedor(models.Model):#Este modelo aun o tiene un form para capturar los datos de la empresa
	nombre_empresa = models.CharField(max_length=50,default="")
	nit = models.CharField(max_length=20)#tipo de campo entero no recibe parametros
	telefono = models.CharField(max_length=50)
	contacto_email = models.EmailField()
	class Meta:
		verbose_name = "Empresa"
		verbose_name_plural = "Empresas"
	def __unicode__(self):#funcion para que se nos devuelva el nombre y no el objeto
	#que hemos registrado
		return '{}'.format(self.nombre_empresa)#en este caso la llave foranea del proveedor
		#y que nos muestre en un select el nombre de la empresa
	

	
#hacer llave foraea hacia la empresa para mostrar la empresa del proveedor

class Perfil(models.Model):
	
	empresa_proveedor = models.ForeignKey(EmpresaProveedor, null=True, blank= False,default="")
	usuario = models.OneToOneField(User)
	direccion = models.TextField(max_length=50, null=True)
	telefono = models.CharField( max_length=50)
	dui = models.CharField( max_length=50, null=True)
	nit = models.CharField( max_length=50, null=True)
	#no me permite importar categoria class
	#scategoria = models.ManyToManyField(Categoria, blank=True)
	class Meta:
		verbose_name = "Perfil"
		verbose_name_plural = "Perfiles"

	def __unicode__(self):#funcion para que se nos devuelva el nombre y no el objeto
	#que hemos registrado
		return '{}'.format(self.usuario)#en este caso la llave foranea del proveedor
		#y que nos muestre en un select el nombre de la empresa
