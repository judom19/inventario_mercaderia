from django.http import HttpResponse
from django.views import View
from django.template.loader import get_template
from productos.models import Pedido_mercaderia
from perfil.models import EmpresaProveedor, Perfil
from base_inventario.render import render_to_pdf

class PedidoPDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pedido_reporte.html')
        pedido = Pedido_mercaderia.objects.all()
        context = {'pedidos': pedido}
        html = template.render(context)
        pdf = render_to_pdf('pdf/pedido_pdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

class EmpresasPDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('listado_empresas.html')
        empresa = EmpresaProveedor.objects.all()
        context = {'empresas': empresa}
        html = template.render(context)
        pdf = render_to_pdf('pdf/empresas_pdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

class PerfilPDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('lista_usuarios.html')
        proveedor = Perfil.objects.all()
        context = {'proveedores': proveedor}
        html = template.render(context)
        pdf = render_to_pdf('pdf/perfil_pdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')
