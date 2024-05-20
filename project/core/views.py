from django.contrib.auth.views import LoginView
from django.shortcuts import render
from.forms import CustomAuthenticationForm
from . import models

def home(request):
    return render(request, 'core/index.html')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'
    
    
    
def logoutpage(request):
    return render(request,'core/logoutpage.html')
    
    