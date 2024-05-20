from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'core'

urlpatterns = [
    path ('',views.home, name='home'),
    path ('login/', views.CustomLoginView.as_view(), name='login'), 
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='core:logoutpage'), name='logout'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
]