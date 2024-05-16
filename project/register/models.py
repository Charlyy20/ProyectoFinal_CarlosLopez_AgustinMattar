from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=255, default='0000000000')
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Direccion(models.Model):
    calle = models.CharField(max_length=255)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=255)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

class Contacto(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=255, default='0000000000')
    contraseña = models.CharField(max_length=255)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
