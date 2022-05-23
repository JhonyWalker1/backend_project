from django.db import models

from cloudinary.models import CloudinaryField
# Create your models here.

class Cliente(models.Model):
    cliente_id=models.AutoField(primary_key=True)
    cliente_nombre = models.CharField(max_length=100)
    cliente_apellido = models.CharField(max_length=100)
    cliente_email = models.EmailField()
    cliente_telefono = models.CharField(max_length=100)
    cliente_direccion = models.CharField(max_length=100)
    cliente_pais = models.CharField(max_length=100)
    cliente_ciudad = models.CharField(max_length=100)
    cliente_fecha_nacimiento = models.DateField()
    cliente_foto = CloudinaryField('image')
    compra_id = models.ForeignKey('Compra', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.cliente_nombre

class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.region_nombre

class Tour(models.Model):
    tour_id = models.AutoField(primary_key=True)
    tour_nombre = models.CharField(max_length=100)
    tour_descripcion = models.TextField()
    tour_itinerario = models.TextField()
    tour_precio = models.DecimalField(max_digits=10,decimal_places=2,default=0,
                                    verbose_name='precio')
    tour_foto = CloudinaryField('image')
    region_id = models.ForeignKey(Region, on_delete=models.CASCADE,related_name='Tour',
                                  to_field='region_id',db_column='region_id',verbose_name='region')
    tour_stock = models.IntegerField(default=0)
    tour_fecha_inicio = models.DateField()
    tour_fecha_fin = models.DateField()
    
    def __str__(self):
        return self.tour_nombre
    
class Compra(models.Model):
    compra_id = models.AutoField(primary_key=True)
    compra_fecha = models.DateField()
    compra_total = models.DecimalField(max_digits=10,decimal_places=2,default=0,
                                    verbose_name='total')
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE,related_name='Compra',
                                  to_field='cliente_id',db_column='cliente_id',verbose_name='cliente')
    tour_id = models.ForeignKey(Tour, on_delete=models.CASCADE,related_name='Compra',
                                  to_field='tour_id',db_column='tour_id',verbose_name='tour')
    compra_cantidad = models.IntegerField(default=0)
    
    def __str__(self):
        return self.compra_tour

    