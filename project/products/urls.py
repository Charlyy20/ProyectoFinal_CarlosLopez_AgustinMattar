from django.urls import path
from . import views
from .forms import LlantaCreateForm, AleronCreateForm, SpoilerCreateForm, IntakeCreateForm, WidebodyCreateForm
from .models import Llanta, Aleron, Spoiler, Intake, Widebody

app_name = 'products'

urlpatterns = [
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    path('llanta/', views.llanta_view, name='llanta'),
    path('spoiler/', views.spoiler_view, name='spoiler'),
    path('aleron/', views.aleron_view, name='aleron'),
    path('intake/', views.intake_view, name='intake'),
    path('widebody/', views.widebody_view, name='widebody'),
    path('llanta/<int:pk>/', views.detalle_llanta, name='detalle_llanta'),
    path('aleron/<int:pk>/', views.detalle_aleron, name='detalle_aleron'),
    path('intake/<int:pk>/', views.detalle_intake, name='detalle_intake'),
    path('spoiler/<int:pk>/', views.detalle_spoiler, name='detalle_spoiler'),
    path('widebody/<int:pk>/', views.detalle_widebody, name='detalle_widebody'),
    #----------------------- Creates -----------------------#
    path('create_llanta/', views.create_product, { 'form_class': LlantaCreateForm, 'redirect_url': 'products:llanta', 'category': 'llanta'}, name='create_llanta'),
    path('create_aleron/', views.create_product, {'form_class': AleronCreateForm,'redirect_url': 'products:aleron','category': 'aleron'}, name='create_aleron'),
    path('create_spoiler/', views.create_product, {'form_class': SpoilerCreateForm,'redirect_url': 'products:spoiler','category': 'spoiler'}, name='create_spoiler'),
    path('create_intake/', views.create_product, {'form_class': IntakeCreateForm,'redirect_url': 'products:intake','category': 'intake'}, name='create_intake'),
    path('create_widebody/', views.create_product, {'form_class': WidebodyCreateForm,'redirect_url': 'products:widebody','category': 'widebody'}, name='create_widebody'),
    #----------------------- Update -----------------------#
    path('update_llanta/<int:pk>/', views.update_product, {'model_class': Llanta,'form_class': LlantaCreateForm,'redirect_url': 'products:llanta'}, name='update_llanta'),
    path('update_aleron/<int:pk>/', views.update_product, {'model_class': Aleron,'form_class': AleronCreateForm,'redirect_url': 'products:aleron'}, name='update_aleron'),
    path('update_spoiler/<int:pk>/', views.update_product, {'model_class': Spoiler,'form_class': SpoilerCreateForm,'redirect_url': 'products:spoiler'}, name='update_spoiler'),
    path('update_intake/<int:pk>/', views.update_product, {'model_class': Intake,'form_class': IntakeCreateForm,'redirect_url': 'products:intake'}, name='update_intake'),
    path('update_widebody/<int:pk>/', views.update_product, {'model_class': Widebody,'form_class': WidebodyCreateForm,'redirect_url': 'products:widebody'}, name='update_widebody'),
    #----------------------- Delete -----------------------#
    path('<int:llanta_id>/delete/', views.delete_llanta, name='delete_llanta'),
    path('<int:aleron_id>/delete_aleron/', views.delete_aleron, name='delete_aleron'),
    path('<int:spoiler_id>/delete_spoiler/', views.delete_spoiler, name='delete_spoiler'),
    path('<int:intake_id>/delete_intake/', views.delete_intake, name='delete_intake'),
    path('<int:widebody_id>/delete_widebody/', views.delete_widebody, name='delete_widebody'),
]