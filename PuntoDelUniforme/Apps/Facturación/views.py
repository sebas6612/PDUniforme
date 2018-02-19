from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from PuntoDelUniforme.utileria import render_pdf

import os
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm

from PuntoDelUniforme.Apps.Productos.models import *
from PuntoDelUniforme.Apps.Facturación.models import *







# Create your views here.
class PDFPrueba(View):
	"""docstring for PDFPrueba
	"""


	def get(self, request, *arg, **kwargs):


		# Ejemplo de como pasar un diccionario 
		#datos = {
		#	"nombres": "Hector",
		#	"apellido": "Jairo",
		#	"edad": 22
		#}

		#datos2 = BlueJean.objects.all()

		#pks_pedido = Factura.objects.all().values("pedido__pk").distinct()
		#datos2 = Pedido.objects.all().exclude(pk__in=pks_pedido)

		#pks_pedido = Factura.objects.all().values("pedido__pk")
		#datos2 = Pedido.objects.all().exclude(pk__in=pks_pedido)


		consulta = Pedido.objects.filter(factura = kwargs.get('id'))

		listaProductos = []
		listaSubtotal = []
		total = 0

		for produc in consulta:
			listaSubtotal.append(produc.subTotal)
			total += produc.subTotal
			if produc.producto == 'p00':
				listaProductos.append('BlueJean')
			if produc.producto == 'p01':
				listaProductos.append('Blusa')
			if produc.producto == 'p02':
				listaProductos.append('Chaqueta')
			if produc.producto == 'p03':
				listaProductos.append('delantal')
			if produc.producto == 'p04':
				listaProductos.append('Guayabera')
			if produc.producto == 'p05':
				listaProductos.append('Pantaloneta')
			if produc.producto == 'p06':
				listaProductos.append('Sudadera')



		pdf = render_pdf("principal/reporte_pdf.html",
			{
			"datos_factura": consulta,
			"producto": listaProductos,
			"subTotal": listaSubtotal,
			"total": total,
			}
		)
		
		return HttpResponse(pdf, content_type="application/pdf")
		