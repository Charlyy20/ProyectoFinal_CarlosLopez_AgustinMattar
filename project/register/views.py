from django.shortcuts import render, redirect, HttpResponse
from . import models, forms 

def register(request):
    return render(request, 'register/register.html')

def register_person(request):
    print("Received a request:", request.method)
    if request.method == 'POST':
        persona = forms.PersonaForm(request.POST)
        direccion = forms.DireccionForm(request.POST)
        contacto = forms.ContactoForm(request.POST)
        if persona.is_valid() and direccion.is_valid() and contacto.is_valid():
            persona_instancia = persona.save()
            direccion_instancia = direccion.save(commit=False)
            direccion_instancia.persona = persona_instancia
            direccion_instancia.save()
            contacto_instancia = contacto.save(commit=False)
            contacto_instancia.persona = persona_instancia
            contacto_instancia.save()
            print("Form is valid and saved.")
            return HttpResponse('OK',content_type="text/plain", status=200)
        else:
            print("Form is not valid:", persona.errors)
    else:
        persona = forms.PersonaForm()
    return render(request, 'register/register.html', {'form': {'persona': persona, 'direccion': direccion, 'contacto': contacto}})
