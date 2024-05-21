from django.contrib.auth.views import LoginView
from django.shortcuts import render
from.forms import CustomAuthenticationForm
from . import models
import os
from django.conf import settings
from django.views.decorators.http import require_GET
from django.http import FileResponse




def home(request):
    return render(request, 'core/index.html')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'
    
    
    
def logoutpage(request):
    return render(request,'core/logoutpage.html')
    
    
    
def aboutus(request):
    return render(request,"core/aboutus.html")




@require_GET
def descargar_cv(request):
    # Ruta al archivo PDF
    pdf_path = os.path.join(settings.STATIC_ROOT, 'core/static/core/assets/media/cvagusmayo2024.pdf')
    # Abre el archivo y lo sirve como respuesta
    return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')