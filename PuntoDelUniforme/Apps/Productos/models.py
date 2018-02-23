from django.db import models
from PuntoDelUniforme.Apps.Clientes.models import *
from PuntoDelUniforme.validators import validarPrecio

# Create your models here.

class Blusa(models.Model):
    Colegio = models.ForeignKey(Colegio, null=False, blank=False, on_delete=models.CASCADE)
    PrecioS = models.PositiveIntegerField(validators=[validarPrecio])
    PrecioM = models.PositiveIntegerField(validators=[validarPrecio])
    PrecioL = models.PositiveIntegerField(validators=[validarPrecio])
    
    def NombreCompleto(self):
        cadena = "Colegio: {0} - Precios S:{1}; M:{2}; L:{3}"
        return cadena.format(self.Colegio, self.PrecioS, self.PrecioM, self.PrecioL)
    
    def __str__(self):
        return self.NombreCompleto()
    
class Pantaloneta(models.Model):
    Colegio = models.ForeignKey(Colegio, null=False, blank=False, on_delete=models.CASCADE)
    PrecioS = models.PositiveIntegerField(validators=[validarPrecio])
    PrecioM = models.PositiveIntegerField(validators=[validarPrecio])
    PrecioL = models.PositiveIntegerField(validators=[validarPrecio])
    
    def NombreCompleto(self):
        cadena = "Colegio: {0} - Precios S:{1}; M:{2}; L:{3}"
        return cadena.format(self.Colegio, self.PrecioS, self.PrecioM, self.PrecioL)
    
    def __str__(self):
        return self.NombreCompleto()
    
class Delantale(models.Model):
    Colegio = models.ForeignKey(Colegio, null=False, blank=False, on_delete=models.CASCADE)
    PrecioS = models.PositiveIntegerField(validators=[validarPrecio])
    PrecioM = models.PositiveIntegerField(validators=[validarPrecio])
    PrecioL = models.PositiveIntegerField(validators=[validarPrecio])
    
    def NombreCompleto(self):
        cadena = "Colegio: {0} - Precios S:{1}; M:{2}; L:{3}"
        return cadena.format(self.Colegio, self.PrecioS, self.PrecioM, self.PrecioL)
    
    def __str__(self):
        return self.NombreCompleto()
    
class BlueJean(models.Model):
    Colegio = models.ForeignKey(Colegio, null=False, blank=False, on_delete=models.CASCADE)
    PrecioS = models.PositiveIntegerField(validators=[validarPrecio])
    PrecioM = models.PositiveIntegerField(validators=[validarPrecio])
    PrecioL = models.PositiveIntegerField(validators=[validarPrecio])
    
    def NombreCompleto(self):
        cadena = "Colegio: {0} - Precios S:{1}; M:{2}; L:{3}"
        return cadena.format(self.Colegio, self.PrecioS, self.PrecioM, self.PrecioL)
    
    def __str__(self):
        return self.NombreCompleto()
    
class Chaqueta(models.Model):   
    Colegio = models.ForeignKey(Colegio, null=False, blank=False, on_delete=models.CASCADE)
    PrecioS = models.PositiveIntegerField(validators=[validarPrecio])
    PrecioM = models.PositiveIntegerField(validators=[validarPrecio])
    PrecioL = models.PositiveIntegerField(validators=[validarPrecio])
    
    def NombreCompleto(self):
        cadena = "Colegio: {0} - Precios S:{1}; M:{2}; L:{3}"
        return cadena.format(self.Colegio, self.PrecioS, self.PrecioM, self.PrecioL)
    
    def __str__(self):
        return self.NombreCompleto()
    
class Guayabera(models.Model):
    Colegio = models.ForeignKey(Colegio, null=False, blank=False, on_delete=models.CASCADE)
    PrecioS = models.PositiveIntegerField(validators=[validarPrecio])
    PrecioM = models.PositiveIntegerField(validators=[validarPrecio])
    PrecioL = models.PositiveIntegerField(validators=[validarPrecio])
    
    def NombreCompleto(self):
        cadena = "Colegio: {0} - Precios S:{1}; M:{2}; L:{3}"
        return cadena.format(self.Colegio, self.PrecioS, self.PrecioM, self.PrecioL)
    
    def __str__(self):
        return self.NombreCompleto()
    
class Sudadera(models.Model):
    Colegio = models.ForeignKey(Colegio, null=False, blank=False, on_delete=models.CASCADE)
    PrecioS = models.PositiveIntegerField(validators=[validarPrecio])
    PrecioM = models.PositiveIntegerField(validators=[validarPrecio])
    PrecioL = models.PositiveIntegerField(validators=[validarPrecio])
    
    def NombreCompleto(self):
        cadena = "Colegio: {0} - Precios S:{1}; M:{2}; L:{3}"
        return cadena.format(self.Colegio, self.PrecioS, self.PrecioM, self.PrecioL)
    
    def __str__(self):
        return self.NombreCompleto()
    
    