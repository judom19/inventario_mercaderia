from django.db import models
from django.contrib.auth.models import User

class EmpresaProveedor(models.Model):
    nombre_empresa = models.CharField(max_length=50, default="")
    nit = models.CharField(max_length=20)
    telefono = models.CharField(max_length=50)
    contacto_email = models.EmailField()

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nombre_empresa

class Perfil(models.Model):
    empresa_proveedor = models.ForeignKey(EmpresaProveedor, null=True, blank=False, on_delete=models.SET_DEFAULT, default="")
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.TextField(max_length=50, null=True)
    telefono = models.CharField(max_length=50)
    dui = models.CharField(max_length=50, null=True)
    nit = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return str(self.usuario)
