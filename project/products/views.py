from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Llanta, Aleron, Spoiler, Intake, Widebody
from .forms import LlantaCreateForm, AleronCreateForm, SpoilerCreateForm, IntakeCreateForm, WidebodyCreateForm
from django.urls import reverse
from django.apps import apps

# ============= Views ============ #

def llanta_view(request):
    llantas = Llanta.objects.all()
    return render(request, 'products/llanta.html', {'llantas': llantas})

def aleron_view(request):
    alerones = Aleron.objects.all()
    return render(request, 'products/aleron.html', {'alerones': alerones})

def spoiler_view(request):
    spoilers = Spoiler.objects.all()
    return render(request, 'products/spoiler.html', {'spoilers': spoilers})

def intake_view(request):
    intakes = Intake.objects.all()
    return render(request, 'products/intake.html', {'intakes': intakes})

def widebody_view(request):
    widebodys = Widebody.objects.all()
    return render(request, 'products/widebody.html', {'widebodys': widebodys})

# ============= Buscador View ============ #

def product_search(request, model, template_name):
    q = request.GET.get("q", "")
    
    if q:
        query = model.objects.filter(marca__icontains=q) | model.objects.filter(modelo__icontains=q)
    else:
        query = model.objects.all()
    context = {"productos": query}
    return render(request, template_name, context)

# ============= Create Views ============ #

def create_product(request, form_class, redirect_url, category):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.categoria = category
            product.save()
            return redirect(redirect_url)
    else:
        form = form_class()
    return render(request, 'products/create.html', {'form': form})

@permission_required('products.can_create_llanta')
def create_llanta(request):
    return create_product(request, LlantaCreateForm, 'products:llanta', 'llanta')

@permission_required('products.can_create_aleron')
def create_aleron(request):
    return create_product(request, AleronCreateForm, 'products:aleron', 'aleron')

@permission_required('products.can_create_spoiler')
def create_spoiler(request):
    return create_product(request, SpoilerCreateForm, 'products:spoiler', 'spoiler')

@permission_required('products.can_create_intake')
def create_intake(request):
    return create_product(request, IntakeCreateForm, 'products:intake', 'intake')

@permission_required('products.can_create_widebody')
def create_widebody(request):
    return create_product(request, WidebodyCreateForm, 'products:widebody', 'widebody')

# ============= Update Views ============ #

def update_product(request, pk, model_class, form_class, redirect_url):
    product = get_object_or_404(model_class, pk=pk)
    if request.method == 'POST':
        form = form_class(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=product)
    return render(request, 'products/update.html', {'form': form})

@permission_required('products.can_update_llanta')
def update_llanta(request, pk):
    return update_product(request, pk, Llanta, LlantaCreateForm, 'products:llanta')

@permission_required('products.can_update_aleron')
def update_aleron(request, pk):
    return update_product(request, pk, Aleron, AleronCreateForm, 'products:aleron')

@permission_required('products.can_update_spoiler')
def update_spoiler(request, pk):
    return update_product(request, pk, Spoiler, SpoilerCreateForm, 'products:spoiler')

@permission_required('products.can_update_intake')
def update_intake(request, pk):
    return update_product(request, pk, Intake, IntakeCreateForm, 'products:intake')

@permission_required('products.can_update_widebody')
def update_widebody(request, pk):
    return update_product(request, pk, Widebody, WidebodyCreateForm, 'products:widebody')

# ============= Delete Views ============ #

@permission_required('products.can_delete_llanta')
def delete_llanta(request, llanta_id):
    llanta = get_object_or_404(Llanta, id=llanta_id)
    llanta.delete()
    return redirect(reverse('products:llanta'))

@permission_required('products.can_delete_aleron')
def delete_aleron(request, aleron_id):
    aleron = get_object_or_404(Aleron, id=aleron_id)
    aleron.delete()
    return redirect(reverse('products:aleron'))

@permission_required('products.can_delete_spoiler')
def delete_spoiler(request, spoiler_id):
    spoiler = get_object_or_404(Spoiler, id=spoiler_id)
    spoiler.delete()
    return redirect(reverse('products:spoiler'))

@permission_required('products.can_delete_intake')
def delete_intake(request, intake_id):
    intake = get_object_or_404(Intake, id=intake_id)
    intake.delete()
    return redirect(reverse('products:intake'))

@permission_required('products.can_delete_widebody')
def delete_widebody(request, widebody_id):
    widebody = get_object_or_404(Widebody, id=widebody_id)
    widebody.delete()
    return redirect(reverse('products:widebody'))

# ============= Details Views ============ #

def detalle_llanta(request, pk):
    llanta = get_object_or_404(Llanta, pk=pk)
    return render(request, 'products/portfolio-details.html', {'producto': llanta})

def detalle_aleron(request, pk):
    aleron = get_object_or_404(Aleron, pk=pk)
    return render(request, 'products/portfolio-details.html', {'producto': aleron})

def detalle_intake(request, pk):
    intake = get_object_or_404(Intake, pk=pk)
    return render(request, 'products/portfolio-details.html', {'producto': intake})

def detalle_spoiler(request, pk):
    spoiler = get_object_or_404(Spoiler, pk=pk)
    return render(request, 'products/portfolio-details.html', {'producto': spoiler})

def detalle_widebody(request, pk):
    widebody = get_object_or_404(Widebody, pk=pk)
    return render(request, 'products/portfolio-details.html', {'producto': widebody})

def portfolio_details(request,):
    return render(request, 'products/portfolio-details.html')
