# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-25 05:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='empresa_proveedor',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='perfil.EmpresaProveedor'),
        ),
    ]