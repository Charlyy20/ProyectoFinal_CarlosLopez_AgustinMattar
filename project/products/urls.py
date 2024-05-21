from django.urls import path
from . import views
from django.contrib.auth.decorators import permission_required
from .models import Llanta, Aleron, Spoiler, Intake, Widebody
from .forms import LlantaCreateForm, AleronCreateForm, SpoilerCreateForm, IntakeCreateForm, WidebodyCreateForm

app_name = 'products'

urlpatterns = [
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    path('llanta/', views.product_search, {'model': Llanta, 'template_name': 'products/llanta.html'}, name='llanta'),
    path('spoiler/', views.product_search, {'model': Spoiler, 'template_name': 'products/spoiler.html'}, name='spoiler'),
    path('aleron/', views.product_search, {'model': Aleron, 'template_name': 'products/aleron.html'}, name='aleron'),
    path('intake/', views.product_search, {'model': Intake, 'template_name': 'products/intake.html'}, name='intake'),
    path('widebody/', views.product_search, {'model': Widebody, 'template_name': 'products/widebody.html'}, name='widebody'),
    
    #----------------------- Detail -----------------------#
    path('llanta/<int:pk>/', views.detalle_llanta, name='detalle_llanta'),
    path('aleron/<int:pk>/', views.detalle_aleron, name='detalle_aleron'),
    path('intake/<int:pk>/', views.detalle_intake, name='detalle_intake'),
    path('spoiler/<int:pk>/', views.detalle_spoiler, name='detalle_spoiler'),
    path('widebody/<int:pk>/', views.detalle_widebody, name='detalle_widebody'),

    #----------------------- Creates -----------------------#
    path('create_llanta/', permission_required('products.can_create_llanta')(views.create_product), {'form_class': LlantaCreateForm, 'redirect_url': 'products:llanta', 'category': 'llanta'}, name='create_llanta'),
    path('create_aleron/', permission_required('products.can_create_aleron')(views.create_product), {'form_class': AleronCreateForm, 'redirect_url': 'products:aleron', 'category': 'aleron'}, name='create_aleron'),
    path('create_spoiler/', permission_required('products.can_create_spoiler')(views.create_product), {'form_class': SpoilerCreateForm, 'redirect_url': 'products:spoiler', 'category': 'spoiler'}, name='create_spoiler'),
    path('create_intake/', permission_required('products.can_create_intake')(views.create_product), {'form_class': IntakeCreateForm, 'redirect_url': 'products:intake', 'category': 'intake'}, name='create_intake'),
    path('create_widebody/', permission_required('products.can_create_widebody')(views.create_product), {'form_class': WidebodyCreateForm, 'redirect_url': 'products:widebody', 'category': 'widebody'}, name='create_widebody'),
    
    #----------------------- Update -----------------------#
    path('update_llanta/<int:pk>/', permission_required('products.can_update_llanta')(views.update_product), {'model_class': Llanta, 'form_class': LlantaCreateForm, 'redirect_url': 'products:llanta'}, name='update_llanta'),
    path('update_aleron/<int:pk>/', permission_required('products.can_update_aleron')(views.update_product), {'model_class': Aleron, 'form_class': AleronCreateForm, 'redirect_url': 'products:aleron'}, name='update_aleron'),
    path('update_spoiler/<int:pk>/', permission_required('products.can_update_spoiler')(views.update_product), {'model_class': Spoiler, 'form_class': SpoilerCreateForm, 'redirect_url': 'products:spoiler'}, name='update_spoiler'),
    path('update_intake/<int:pk>/', permission_required('products.can_update_intake')(views.update_product), {'model_class': Intake, 'form_class': IntakeCreateForm, 'redirect_url': 'products:intake'}, name='update_intake'),
    path('update_widebody/<int:pk>/', permission_required('products.can_update_widebody')(views.update_product), {'model_class': Widebody, 'form_class': WidebodyCreateForm, 'redirect_url': 'products:widebody'}, name='update_widebody'),
    
    #----------------------- Delete -----------------------#
    path('<int:llanta_id>/delete/', permission_required('products.can_delete_llanta')(views.delete_llanta), name='delete_llanta'),
    path('<int:aleron_id>/delete_aleron/', permission_required('products.can_delete_aleron')(views.delete_aleron), name='delete_aleron'),
    path('<int:spoiler_id>/delete_spoiler/', permission_required('products.can_delete_spoiler')(views.delete_spoiler), name='delete_spoiler'),
    path('<int:intake_id>/delete_intake/', permission_required('products.can_delete_intake')(views.delete_intake), name='delete_intake'),
    path('<int:widebody_id>/delete_widebody/', permission_required('products.can_delete_widebody')(views.delete_widebody), name='delete_widebody'),
    
    #----------------------- Search mejorado -----------------------#    
    path('llantas/', views.product_search, {'model': Llanta, 'template_name': 'products/llanta.html'}, name='llanta_search'),
    path('alerones/', views.product_search, {'model': Aleron, 'template_name': 'products/aleron.html'}, name='aleron_search'),
    path('spoilers/', views.product_search, {'model': Spoiler, 'template_name': 'products/spoiler.html'}, name='spoiler_search'),
    path('intakes/', views.product_search, {'model': Intake, 'template_name': 'products/intake.html'}, name='intake_search'),
    path('widebody/', views.product_search, {'model': Widebody, 'template_name': 'products/widebody.html'}, name='widebody_search'),

]