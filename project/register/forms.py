from django import forms
from .models import Persona, Contacto

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'fecha_nacimiento']

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['email', 'telefono']
        