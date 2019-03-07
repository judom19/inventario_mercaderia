from django import forms
from app.productos.models import Producto,Pedido_mercaderia

#creando la clase de el formulario para Registar datos
# desde nel template productos_form.html
class ProductoForm(forms.ModelForm):#esta es la clase que se crea para poder
#nuestra vista
	#la clase ProductoForm esta heredando todas los metos de form.ModelForm
	class Meta:#modelo del cual vamos a crear nuestro formulario
		model = (Producto)#guardando el modelo Producto dentro de la variable model
		fields = [# la clase  meta nos sirve para usar los metadatos en nuestro modelo.
		#ordenar dato entre otras cosas

		#colocando todos los campos del modelo Productos
		#para utilizarlos
			'nombre',
			'descripcion',
			'marca',
			'precio_unitario',
			'inventario',
			'factor_de_empaque',			
			'empresa_proveedor',
			'categoria',


		]
		# creando los label de nuestro formulario
		# o la etiquetas que contendra nuestro formulario
		labels = {
			'nombre':			'Nombre',
			'descripcion':		'Descripcion',
			'marca':			'Marca',
			'precio_unitario':	'Precio/unidad',
			'factor_de_empaque': 'factor_de_empaque',
			'inventario'		: 'inventario',
			# 'fecha_compra':		'Fecha de Compra',
			'empresa_proveedor':		'Proveedor',
			'categoria':	'Categoria',

		}
		widgets	= {
		# #Creando los widgets
		# #El widget maneja la representacion del HTML 
		# #y la extraccion de datos de un diccionario GET / POST que corresponde al widget.
		# #dan la forma html

		 	'nombre':forms.TextInput(attrs={'class':'form-group'}),#como atributo madamos 
		 	#la clase from control de boostrap
		 	'descripcion':forms.Textarea(attrs={'cols': 56, 'rows': 5}),
		 	'marca':forms.TextInput(attrs={'class':'form-group'}),
		 	'precio_unitario':forms.TextInput(attrs={'class':'form-group'}),
		 	'factor_de_empaque':forms.Select(attrs={'class':'form-group'}),
		 	'inventario':forms.TextInput(attrs={'class':'form-group'}),
		 	# 'fecha_compra':forms.TextInput(attrs={'class':'form-control'}),
		 	'empresa_proveedor':forms.Select(attrs={'class':'form-control'}),#proveedor es una llave foranea
		 	'categoria':forms.CheckboxSelectMultiple(attrs={'class':'form-check-inline'}),#tipo_producto es un atributo con una relacion
		# 	#de muchos a muchos, y se utiliza un CheckboxSelectMultiple

		}
		# #form para hacer pedidos de productos

class Pedido_mercaderiaForm(forms.ModelForm):#esta es la clase que se crea para poder
#nuestra vista
	#la clase ProductoForm esta heredando todas los metos de form.ModelForm
	class Meta:#modelo del cual vamos a crear nuestro formulario
		model = Pedido_mercaderia #guardando el modelo Producto dentro de la variable model
		fields = [# la clase  meta nos sirve para usar los metadatos en nuestro modelo.
		#ordenar dato entre otras cosas

		#colocando todos los campos del modelo Productos
		#para utilizarlos
			#agregar campo de numero de orden
			'producto_a_pedir',
			'cantidad',
			
			


		]
		
		labels = {
			'producto_a_pedir':		'Elegir Mercaderia',
			'cantidad':				'Cuantos Articulos desea pedir?',
		
		
		}
		widgets	= {
		
			'producto_a_pedir':forms.Select(attrs={'class':'form-control'}),
			'cantidad':forms.TextInput(attrs={'class':'form-control'}),
			'empresa_proveedor':forms.Select(attrs={'class':'form-control'}),
		}
