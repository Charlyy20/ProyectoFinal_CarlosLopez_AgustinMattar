from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    path('llanta/', views.llanta_view, name='llanta'),
    path('spoiler/', views.spoiler_view, name='spoiler'),
    path('aleron/', views.aleron_view, name='aleron'),
    path('intake/', views.intake_view, name='intake'),
    path('widebody/', views.widebody_view, name='widebody'),
    #----------------------- Creates -----------------------#
    path('create_llanta/', views.create_llanta, name='create_llanta'),
    path('create_aleron/', views.create_aleron, name='create_aleron'),
    path('create_spoiler/', views.create_spoiler, name='create_spoiler'),
    path('create_intake/', views.create_intake, name='create_intake'),
    path('create_widebody/', views.create_widebody, name='create_widebody'),
    #----------------------- Update -----------------------#


]