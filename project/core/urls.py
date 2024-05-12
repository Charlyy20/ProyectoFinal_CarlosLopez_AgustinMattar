from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path ('',views.home, name='home'),
    path ('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path ('login/', views.CustomLoginView.as_view(), name='login'),
]