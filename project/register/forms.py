from django import forms
from .models import Persona, Direccion, Contacto

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'fecha_nacimiento']

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'numero', 'ciudad']

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['email', 'telefono']