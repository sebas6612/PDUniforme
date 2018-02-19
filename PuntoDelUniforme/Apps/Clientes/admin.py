from django.contrib import admin
from PuntoDelUniforme.Apps.Clientes.models import *


class ColegioAdmin(admin.ModelAdmin):
	search_fields = (
		'Nombre',
		)

admin.site.register(Colegio, ColegioAdmin)


