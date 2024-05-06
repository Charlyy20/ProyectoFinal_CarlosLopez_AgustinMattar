from django.contrib import admin
from .models import Persona, Direccion, Contacto

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento')

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('calle', 'numero', 'ciudad', 'persona')

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('email', 'telefono', 'persona')