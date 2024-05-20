from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'core'

urlpatterns = [
    path ('',views.home, name='home'),
    path ('login/', views.CustomLoginView.as_view(), name='login'), 
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='core:logoutpage'), name='logout'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
