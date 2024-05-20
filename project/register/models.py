from django.db import models
from django.contrib.auth.models import User


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Contacto(models.Model):
    email = models.EmailField()
    telefono = models.CharField(max_length=255)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    
class Cuenta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    
