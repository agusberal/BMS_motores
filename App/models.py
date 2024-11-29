from django.db import models

# Create your models here.
class Vehiculos(models.Model):
    Codigo = models.AutoField(primary_key=True)  
    Modelo = models.TextField(max_length=30)     
    Marca = models.TextField(max_length=30)
    Desripcion = models.TextField(max_length=150, null=True)    
    Precio = models.IntegerField()  
    Cantidad = models.PositiveIntegerField()  # Stock disponible                 
    Imagen = models.ImageField(upload_to="autos", null=True)  
    
    def __str__(self):
        return str(self.Codigo)  # Devuelve el código del vehículo como una cadena
