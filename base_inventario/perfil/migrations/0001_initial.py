# Generated by Django 4.2.7 on 2023-11-05 00:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaProveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(default='', max_length=50)),
                ('nit', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=50)),
                ('contacto_email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.TextField(max_length=50, null=True)),
                ('telefono', models.CharField(max_length=50)),
                ('dui', models.CharField(max_length=50, null=True)),
                ('nit', models.CharField(max_length=50, null=True)),
                ('empresa_proveedor', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='perfil.empresaproveedor')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
    ]
