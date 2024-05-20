from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Products, Llanta, Aleron, Spoiler, Intake, Widebody
from .forms import LlantaCreateForm, AleronCreateForm, SpoilerCreateForm, IntakeCreateForm, WidebodyCreateForm

# ============= Views ============ #

#def home(request):
    
    #q = request.GET.get("q", None)

    #if q:
        #query = Products.objects.filter(marca__icontains=q)
        
    #else:
        #query = Products.objects.all()
    #context = {"productos": query}
    #return render(request, 'core/index.html', context)

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

# ============= Buscador View ============ #

# ============= Froms Create Views ============ #

def create_llanta(request):
    if request.method == 'POST':
        form_llanta = LlantaCreateForm(request.POST)
        if form_llanta.is_valid():
            form_llanta.save()
            return redirect('products:llanta')
    else:
        form_llanta = LlantaCreateForm()
    return render(request, 'products/create.html',context={'form_llantacreate': form_llanta})

def create_aleron(request):
    if request.method == 'POST':
        form_aleron = AleronCreateForm(request.POST)
        if form_aleron.is_valid():
            form_aleron.save()
            return redirect('products:aleron')
    else:
        form_aleron = AleronCreateForm()
    return render(request, 'products/create.html',context={'form_aleroncreate': form_aleron})

def create_spoiler(request):
    if request.method == 'POST':
        form_spoiler = SpoilerCreateForm(request.POST)
        if form_spoiler.is_valid():
            form_spoiler.save()
            return redirect('products:spoiler')
    else:
        form_spoiler = SpoilerCreateForm()
    return render(request, 'products/create.html',context={'form_spoilercreate': form_spoiler})

def create_intake(request):
    if request.method == 'POST':
        form_intake = IntakeCreateForm(request.POST)
        if form_intake.is_valid():
            form_intake.save()
            return redirect('products:intake')
    else:
        form_intake = IntakeCreateForm()
    return render(request, 'products/create.html',context={'form_intakecreate': form_intake})

def create_widebody(request):
    if request.method == 'POST':
        form_widebody = WidebodyCreateForm(request.POST)
        if form_widebody.is_valid():
            form_widebody.save()
            return redirect('products:widebody')
    else:
        form_widebody = WidebodyCreateForm()
    return render(request, 'products/create.html',context={'form_widebodycreate': form_widebody})

# ============= Froms Update Views ============ #

class LlantaUpdateView(UpdateView):
    model= Llanta
    fields = '__all__'
    template_name = 'products/update.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('products:llanta', kwargs={'pk': pk})

# ============= Froms Delete Views ============ #

def delete_llanta(request, pk:int):
    query = Llanta.objects.get(id=pk)
    if request.method == 'POST':
        query.delete()
        return redirect('products:llanta')
    return render(request, 'products/create.html',context={'form_llantacreate': query})

# ============= Details Views ============ #

def portfolio_details(request,):
    return render(request, 'products/portfolio-details.html')

#def product_detail(request, pk):
    query = Llanta.objects.get(id=pk)
    return render(request, 'products/portfolio_details.html', {'product': query})

#def portfolio_details(request,pk):
    print(pk)
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return HttpResponse(status=404)
            
    return render(request, 'products/portfolio-details.html', {'product': product})



