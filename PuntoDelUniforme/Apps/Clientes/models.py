from django.db import models

class Colegio(models.Model):
    Nombre = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.Nombre
    
