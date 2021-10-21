from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from app.productos.models import Pedido_mercaderia
from app.perfil.models  import EmpresaProveedor,Perfil
from base_sistema.render import render_to_pdf
from django.contrib.auth.models import Permission, User

class pedidoPDF(View):
    def get(self, request, *args, **kwargs):
        template=get_template('pedido_reporte.html')
        pedido=Pedido_mercaderia.objects.all()
        context={'pedidos':pedido}
        html=template.render(context)
        pdf= render_to_pdf('pdf/pedido_pdf.html',context)
        return HttpResponse(pdf, content_type='application/pdf')


class empresasPDF(View):
    def get(self, request, *args, **kwargs):
        template=get_template('listado_empresas.html')
        empresa=EmpresaProveedor.objects.all()
        context={'empresas':empresa}
        html=template.render(context)
        pdf= render_to_pdf('pdf/empresas_pdf.html',context)
        return HttpResponse(pdf, content_type='application/pdf')

class perfilPDF(View):
    def get(self, request, *args, **kwargs):
        template=get_template('lista_usuarios.html')
        proveedor=Perfil.objects.all()
        context={'proveedores':proveedor}
        html=template.render(context)
        pdf= render_to_pdf('pdf/perfil_pdf.html',context)
        return HttpResponse(pdf, content_type='application/pdf')
        