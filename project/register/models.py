from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Direccion(models.Model):
    calle = models.CharField(max_length=255)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=255)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Contacto(models.Model):
    email = models.EmailField()
    telefono = models.CharField(max_length=255)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
