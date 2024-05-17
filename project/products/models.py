from django.db import models

class Products(models.Model):
    CATEGORIES = [
        ('llanta', 'Llanta'),
        ('aleron', 'Aleron'),
        ('spoiler', 'Spoiler'),
        ('intake', 'Intake'),
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

class Llanta(Products):
    diametro = models.DecimalField(max_digits=5, decimal_places=2)
    medida_centro = models.CharField(max_length=15)

class Aleron(Products):
    altura = models.CharField(max_length=15)
    

class Spoiler(Products):
    pass


class Intake(Products):
    pass

class Widebody(Products):
    pass
