from django import forms
from .models import Perfil
from .models import EmpresaProveedor
from django.contrib.auth.models import Permission, User


class PerfilCrear(forms.ModelForm):
    class Meta:
        model = (Perfil)
        fields =('empresa_proveedor','usuario','direccion','telefono','dui','nit',)
	labels = {
	'usuario':			'Usuario',
	'empresa_proveedor': 'Empresa',
	'direccion':		'Direccion',
	'telefono':			'Telefono',
	'dui':				'DUI',
	'nit':				'NIT',

	}
	


class UsuarioCrear(forms.ModelForm):
    class Meta:
        model = (User)
        fields = ('username','first_name','last_name','password',)#campos traidos del modelo user

	# labels = {
	# 	'username':			'Usuario',
	# 	'first_name':		'Nombre',
	# 	'last_name':		'Apellido',
	# 	'password':			'Contrasena',
		
		

	# 	}

	# widgets	= {
	# #Creando los widgets
	# #El widget maneja la representacion del HTML 
	# #y la extraccion de datos de un diccionario GET / POST que corresponde al widget.
	# #dan la forma html

	# 	'username':forms.TextInput(attrs={'class':'form-control'}),#como atributo madamos 
	# 	#la clase from control de boostrap
	# 	'first_name':forms.TextInput(attrs={'class':'form-control'}),
	# 	'last_name':forms.TextInput(attrs={'class':'form-control'}),
	# 	'password':forms.TextInput(attrs={'class':'form-control'}),
		

				# }

class EmpresaCrear(forms.ModelForm):
	class Meta:
		model = (EmpresaProveedor)
		fields = ('nombre_empresa','nit','telefono','contacto_email')

	# labels = {
		
	# 	'nombre_empresa':	'nombre_empresa',
	# 	'nit':		        'nit',
	# 	'telefono':		    'telefono',
	# 	'contacto_email':	'contacto_email',
		
	# 	}


	# widgets	= {
		
		
	# 	'nombre_empresa':forms.TextInput(attrs={'class':'form-control'}),#como atributo madamos 
	# 	#la clase from control de boostrap
	# 	'nit':forms.TextInput(attrs={'class':'form-control'}),
	# 	'telefono':forms.TextInput(attrs={'class':'form-control'}),
	# 	'contacto_email':forms.TextInput(attrs={'class':'form-control'}),
		

	# 	}
