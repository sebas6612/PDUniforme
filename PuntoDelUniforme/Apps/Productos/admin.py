from django.contrib import admin
from PuntoDelUniforme.Apps.Productos.models import *


class BluJeanAdmin(admin.ModelAdmin):
	list_display = (
		'Colegio',
		'PrecioS',
		'PrecioM',
		'PrecioL',
		)
	search_fields = (
		'Colegio__Nombre',
		)

class BlusaAdmin(admin.ModelAdmin):
	list_display = (
		'Colegio',
		'PrecioS',
		'PrecioM',
		'PrecioL',
		)
	search_fields = (
		'Colegio__Nombre',
		)

class PantalonetaAdmin(admin.ModelAdmin):
	list_display = (
		'Colegio',
		'PrecioS',
		'PrecioM',
		'PrecioL',
		)
	search_fields = (
		'Colegio__Nombre',
		)

class DelantaleAdmin(admin.ModelAdmin):
	list_display = (
		'Colegio',
		'PrecioS',
		'PrecioM',
		'PrecioL',
		)
	search_fields = (
		'Colegio__Nombre',
		)

class ChaquetaAdmin(admin.ModelAdmin):
	list_display = (
		'Colegio',
		'PrecioS',
		'PrecioM',
		'PrecioL',
		)
	search_fields = (
		'Colegio__Nombre',
		)

class GuayaberaAdmin(admin.ModelAdmin):
	list_display = (
		'Colegio',
		'PrecioS',
		'PrecioM',
		'PrecioL',
		)
	search_fields = (
		'Colegio__Nombre',
		)

class SudaderaAdmin(admin.ModelAdmin):
	list_display = (
		'Colegio',
		'PrecioS',
		'PrecioM',
		'PrecioL',
		)
	search_fields = (
		'Colegio__Nombre',
		)


admin.site.register(Blusa, BlusaAdmin)
admin.site.register(Pantaloneta, PantalonetaAdmin)
admin.site.register(Delantale, DelantaleAdmin)
admin.site.register(BlueJean, BluJeanAdmin)
admin.site.register(Chaqueta, ChaquetaAdmin)
admin.site.register(Guayabera, GuayaberaAdmin)
admin.site.register(Sudadera, SudaderaAdmin)
