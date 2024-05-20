from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from.models import Cuenta
from . import forms

def register(request):
    return render(request, 'register/register.html')

def register_person(request):
    print("Received a request:", request.method)
    if request.method == 'POST':
        persona = forms.PersonaForm(request.POST)
        contacto = forms.ContactoForm(request.POST)
        user_form = UserCreationForm(request.POST)
        if persona.is_valid() and contacto.is_valid() and user_form.is_valid():
            user_instancia = user_form.save()
            persona_instancia = persona.save()
            contacto_instancia = contacto.save(commit=False)
            contacto_instancia.persona = persona_instancia
            contacto_instancia.save()
            cuenta = Cuenta.objects.create(user=user_instancia, persona=persona_instancia)
            print("Form is valid and saved.")
            return HttpResponse('OK',content_type="text/plain", status=200)
        else:
            print("Form Invalido", persona.errors)           
    else:
        persona = forms.PersonaForm()
    return render(request, 'register/register.html', {'form': {'persona': persona, 'cuenta': user_form, 'contacto': contacto}})
