from django.contrib import admin
from .models import Persona, Contacto, Cuenta

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento')


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('email', 'telefono', 'persona')

@admin.register(Cuenta)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('user', 'persona')