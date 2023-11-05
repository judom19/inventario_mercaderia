from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from .views import PedidoPDF, EmpresasPDF, PerfilPDF
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('productos/', include('productos.urls')),
    path('perfil/', include('perfil.urls')),
    path('pedido_pdf/', login_required(PedidoPDF.as_view()), name='pedido_pdf'),
    path('empresas_pdf/', login_required(EmpresasPDF.as_view()), name='empresas_pdf'),
    path('perfiles_pdf/', login_required(PerfilPDF.as_view()), name='perfiles_pdf'),
]
