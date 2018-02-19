from django.db import models
from PuntoDelUniforme.Apps.Clientes.models import *
from PuntoDelUniforme.Apps.Productos.models import *
import datetime


# Create your models here.

opciones_producto = [
    ('p00','BlueJeans'), 
    ('p01','Blusas'), 
    ('p02','Chaquetas'), 
    ('p03','Delantales'), 
    ('p04','Guayaberas'),
    ('p05','Pantalonetas'),
    ('p06','Sudaderas')
]
#opciones_producto.append(('p05','Pantalonetas'))
#opciones_producto.append(('p06','Sudaderas'))


class Pedido(models.Model):
    
    Colegio = models.ForeignKey(Colegio, null=False, blank=False, on_delete=models.CASCADE)
    producto = models.CharField(max_length=3, choices = opciones_producto)
    cantidad = models.PositiveIntegerField()
    talla = models.PositiveIntegerField()

    def NombreCompleto(self):

        indice = int(self.producto[2])
        print_producto = opciones_producto[indice][1]
        cadena = "{0} {1} talla {2} ({3})"

        #subTotal = Blusa.objects.get(id = 1)
        #x = subTotal.PrecioM
        return cadena.format(self.cantidad, print_producto, self.talla, self.subTotal)

    
    def __str__(self):
        return self.NombreCompleto()

    def _getSubTotal(self):

        if self.producto == 'p00':
            
            consultaProducto = BlueJean.objects.get(Colegio_id = self.Colegio_id)

            if self.talla < 10:
                return consultaProducto.PrecioS * self.cantidad
            elif self.talla < 16:
                return consultaProducto.PrecioM * self.cantidad
            else:
                return consultaProducto.PrecioL * self.cantidad

        elif self.producto == 'p01':

            consultaProducto = Blusa.objects.get(Colegio_id = self.Colegio_id)

            if self.talla < 10:
                return consultaProducto.PrecioS * self.cantidad
            elif self.talla < 16:
                return consultaProducto.PrecioM * self.cantidad
            else:
                return consultaProducto.PrecioL * self.cantidad

        elif self.producto == 'p02':

            consultaProducto = Chaqueta.objects.get(Colegio_id = self.Colegio_id)

            if self.talla < 10:
                return consultaProducto.PrecioS * self.cantidad
            elif self.talla < 16:
                return consultaProducto.PrecioM * self.cantidad
            else:
                return consultaProducto.PrecioL * self.cantidad

        elif self.producto == 'p03':

            consultaProducto = Delantale.objects.get(Colegio_id = self.Colegio_id)

            if self.talla < 10:
                return consultaProducto.PrecioS * self.cantidad
            elif self.talla < 16:
                return consultaProducto.PrecioM * self.cantidad
            else:
                return consultaProducto.PrecioL * self.cantidad

        elif self.producto == 'p04':

            consultaProducto = Guayabera.objects.get(Colegio_id = self.Colegio_id)

            if self.talla < 10:
                return consultaProducto.PrecioS * self.cantidad
            elif self.talla < 16:
                return consultaProducto.PrecioM * self.cantidad
            else:
                return consultaProducto.PrecioL * self.cantidad

        elif self.producto == 'p05':

            consultaProducto = Pantaloneta.objects.get(Colegio_id = self.Colegio_id)

            if self.talla < 10:
                return consultaProducto.PrecioS * self.cantidad
            elif self.talla < 16:
                return consultaProducto.PrecioM * self.cantidad
            else:
                return consultaProducto.PrecioL * self.cantidad

        elif self.producto == 'p06':

            consultaProducto = Sudadera.objects.get(Colegio_id = self.Colegio_id)

            if self.talla < 10:
                return consultaProducto.PrecioS * self.cantidad
            elif self.talla < 16:
                return consultaProducto.PrecioM * self.cantidad
            else:
                return consultaProducto.PrecioL * self.cantidad        

    
    subTotal = property(_getSubTotal)
        
    
class Factura(models.Model):

    #def PedidosDisponibles():
    #    pks_pedido = Factura.objects.all().values("pedido__pk").distinct()
    #    pedidos_disponibles = Pedido.objects.all().exclude(pk__in=pks_pedido)
    #    return pedidos_disponibles


    pedido = models.ManyToManyField(Pedido)
    fecha_pedido = models.DateField()


    
    def NombreCompleto(self):
        cadena = "Fecha: {0}, Total: {1}"
        
        return cadena.format(self.fecha_pedido, self.Total)

    
    def __str__(self):
        return self.NombreCompleto()

    def _getTotal(self):
        
        consultaPedido = Pedido.objects.filter(factura = self.id)
        total = 0
        for totalPedido in consultaPedido:
            total += totalPedido.subTotal
        return total

    Total = property(_getTotal)


#class Deuda(models.Model):
    
        
    
    
    
    