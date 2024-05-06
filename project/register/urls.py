from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_person/', views.register_person, name='register_person'),
]