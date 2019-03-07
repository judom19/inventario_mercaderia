"""base_sistema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url,include
# from django.contrib import admin
# from django.contrib.auth.views import login

# # from django.contrib.auth import views as auth_views
# # from django.views.generic.base import TemplateView


from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from base_sistema.views import pedidoPDF,empresasPDF,perfilPDF
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),#importando las urls del 
    #admin que trae django por defecto
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^productos/', include('app.productos.urls', namespace="productos")),#name_space
    #son los nombres de las urls globalesy 'app.productos.urls' es la ruta del archivo  
    url(r'^perfil/', include('app.perfil.urls',namespace="perfil")),
    ## REPORTES GENERALES
    url(r'^pedido_pdf/',pedidoPDF.as_view(), name='pedido_pdf'),
    url(r'^empresas_pdf/',empresasPDF.as_view(), name='empresas_pdf'),
    url(r'^perfiles_pdf/',perfilPDF.as_view(), name='perfiles_pdf'),


]


