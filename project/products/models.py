from django.db import models

class Productos(models.Model):
    CATEGORIES = [
        ('llantas', 'Llantas'),
        ('alerones', 'Alerones'),
        ('spoilers', 'Spoilers'),
        ('intakes', 'Intakes'),
        ('widebody', 'Widebody'),
        ]
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    material = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=30, choices=CATEGORIES, default='llanta')
    descripcion = models.TextField()

    class Meta:
        abstract = True
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"

class Llantas(Productos):
    diametro = models.DecimalField(max_digits=5, decimal_places=2)
    medida_centro = models.CharField(max_length=15)

class Aleron(Products):
    altura = models.CharField(max_length=15)
    

class Spoilers(Productos):
    pass


class Intakes(Productos):
    pass

class Widebody(Productos):
    pass
