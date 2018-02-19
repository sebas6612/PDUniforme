from django.contrib import admin
from PuntoDelUniforme.Apps.Facturación.models import *

# Register your models here.

class FacturaAdmin(admin.ModelAdmin):
	#exclude = ('') exlulle un campo para que no se muestre
	list_display = (
		'fecha_pedido',
		'_getTotal',
		'id',
		)



#class PedidoAdmin(admin.ModelAdmin):


admin.site.register(Factura, FacturaAdmin)
admin.site.register(Pedido)


