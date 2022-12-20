from django.db import models

class Venta(models.Model):
    nombre      = models.CharField(primary_key=True,max_length=63, verbose_name='Nombre')
    fecha       = models.IntegerField(verbose_name='Fecha')
    precio      = models.IntegerField(verbose_name='Precio')
    descripcion = models.CharField(max_length=50, verbose_name='Descripcion')

    def __str__(self):
        Lista="Nombre: "+self.nombre+"Fecha: "+str(self.fecha)+"Precio: "+str(self.precio)+"Descripcion: "+self.descripcion
        return Lista

class Gasto(models.Model):
   fecha       = models.CharField(max_length=10,verbose_name='Fecha')
   detalle     = models.CharField(max_length=30, verbose_name='Detalle')
   precio      = models.IntegerField(verbose_name='Precio')
   cantidad    = models.IntegerField(verbose_name='Cantidad')

   def __str__(self):
       Lista1="Fecha: "+self.fecha+"Detalle: "+self.detalle+"Precio: "+str(self.precio)+"Cantidad: "+str(self.cantidad)
       return Lista1