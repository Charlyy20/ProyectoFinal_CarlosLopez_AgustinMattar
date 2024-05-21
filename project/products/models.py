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
    imagen = models.ImageField(upload_to='products', null=True, blank=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"

class Llanta(Products):
    diametro = models.DecimalField(max_digits=5, decimal_places=0)
    medida_centro = models.CharField(max_length=15)
    
    class Meta:
        permissions = [
            ("can_create_llanta", "Can create Llanta"),
            ("can_update_llanta", "Can update Llanta"),
            ("can_delete_llanta", "Can delete Llanta"),
        ]

class Aleron(Products):
    altura = models.CharField(max_length=15)
    
    class Meta:
        permissions = [
            ("can_create_aleron", "Can create Aleron"),
            ("can_update_aleron", "Can update Aleron"),
            ("can_delete_aleron", "Can delete Aleron"),
        ]
    

class Spoiler(Products):
    pass

    class Meta:
        permissions = [
            ("can_create_spoiler", "Can create Spoiler"),
            ("can_update_spoiler", "Can update Spoiler"),
            ("can_delete_spoiler", "Can delete Spoiler"),
        ]


class Intake(Products):
    pass

    class Meta:
        permissions = [
            ("can_create_intake", "Can create Intake"),
            ("can_update_intake", "Can update Intake"),
            ("can_delete_intake", "Can delete Intake"),
        ]

class Widebody(Products):
    pass

    class Meta:
        permissions = [
            ("can_create_widebody", "Can create Widebody"),
            ("can_update_widebody", "Can update Widebody"),
            ("can_delete_widebody", "Can delete Widebody"),
        ]
