from django.core.exceptions import ValidationError


def validarPrecio(value):
	if value < 5000:
		raise ValidationError('Valor demasiado bajo')