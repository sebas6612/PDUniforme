from django.contrib import admin
from PuntoDelUniforme.Apps.Facturación.models import *
from django.shortcuts import render

# Register your models here.

def generarFactura(modeladmin, request, queryset):

	return redirect('PDFPrueba')
generarFactura.short_description = 'Generar reporte en pdf'
	


class FacturaAdmin(admin.ModelAdmin):
	#exclude = ('') exclulle un campo para que no se muestre
	list_display = (
		'fecha_pedido',
		'_getTotal',
		'id',
		)

	actions = [generarFactura, ]




#class PedidoAdmin(admin.ModelAdmin):


admin.site.register(Factura, FacturaAdmin)
admin.site.register(Pedido)


