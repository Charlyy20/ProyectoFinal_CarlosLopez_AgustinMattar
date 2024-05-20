from django.urls import path
from . import views
from .models import Products, Llanta, Aleron, Spoiler, Intake, Widebody

app_name = 'products'

urlpatterns = [
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    path('llanta/', views.product_search, {'model': Llanta, 'template_name': 'products/llanta.html'}, name='llanta'),
    path('spoiler/', views.product_search, {'model': Spoiler, 'template_name': 'products/spoiler.html'}, name='spoiler'),
    path('aleron/', views.product_search, {'model': Aleron, 'template_name': 'products/aleron.html'}, name='aleron'),
    path('intake/', views.product_search, {'model': Intake, 'template_name': 'products/intake.html'}, name='intake'),
    path('widebody/', views.product_search, {'model': Widebody, 'template_name': 'products/widebody.html'}, name='widebody'),
    
    #----------------------- Creates -----------------------#
    path('create_llanta/', views.create_llanta, name='create_llanta'),
    path('create_aleron/', views.create_aleron, name='create_aleron'),
    path('create_spoiler/', views.create_spoiler, name='create_spoiler'),
    path('create_intake/', views.create_intake, name='create_intake'),
    path('create_widebody/', views.create_widebody, name='create_widebody'),
    #----------------------- Update -----------------------#
    
    
    #----------------------- Search mejorado -----------------------#    
    path('llantas/', views.product_search, {'model': Llanta, 'template_name': 'products/llanta.html'}, name='llanta_search'),
    path('alerones/', views.product_search, {'model': Aleron, 'template_name': 'products/aleron.html'}, name='aleron_search'),
    path('spoilers/', views.product_search, {'model': Spoiler, 'template_name': 'products/spoiler.html'}, name='spoiler_search'),
    path('intakes/', views.product_search, {'model': Intake, 'template_name': 'products/intake.html'}, name='intake_search'),
    path('widebody/', views.product_search, {'model': Widebody, 'template_name': 'products/widebody.html'}, name='widebody_search'),
    


]