from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('llantas/', views.llantas_view, name='llantas'),
    path('spoilers/', views.spoilers_view, name='spoilers'),
    path('alerones/', views.alerones_view, name='alerones'),
    path('intakes/', views.intakes_view, name='intakes'),
    path('widebody/', views.widebody_view, name='widebody'),
]