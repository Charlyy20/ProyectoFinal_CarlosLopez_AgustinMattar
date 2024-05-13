from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path ('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('llanta/', views.llanta_view, name='llanta'),
    path('spoiler/', views.spoiler_view, name='spoiler'),
    path('aleron/', views.aleron_view, name='aleron'),
    path('intake/', views.intake_view, name='intake'),
    path('widebody/', views.widebody_view, name='widebody'),
]