from django.shortcuts import render
from .models import Products, Llanta, Aleron, Spoiler, Intake, Widebody

def llanta_view(request):
    return render(request, 'products/llanta.html')

def spoiler_view(request):
    return render(request, 'products/spoiler.html')

def aleron_view(request):
    return render(request, 'products/aleron.html')

def intake_view(request):
    return render(request, 'products/intake.html')

def widebody_view(request):
    return render(request, 'products/widebody.html')

#-----------------------------------------------------------------------------------#

def portfolio_details(request):
    return render(request, 'products/portfolio-details.html')
def llanta(request):
    q = request.GET.get(['q'], None)
    if q:
        print(q)
        products = Llanta.objects.filter(marca__icontains=q)
    else:
        products = Llanta.objects.all()
        
    context = {"products": products}
    return render(request, 'products/llanta.html', context)

#def llanta(request):
    q = request.GET.get('q', '')
    products = Aleron.objects.filter(categoria='aleron', marca__icontains=q)
    return render(request, 'products/aleron.html', {'products': products})

#def llanta(request):
    q = request.GET.get('q', '')
    products = Spoiler.objects.filter(categoria='spoiler', marca__icontains=q)
    return render(request, 'products/spoiler.html', {'products': products})

#def llanta(request):
    q = request.GET.get('q', '')
    products = Intake.objects.filter(categoria='intake', marca__icontains=q)
    return render(request, 'products/intake.html', {'products': products})

#def llanta(request):
    q = request.GET.get('q', '')
    products = Widebody.objects.filter(categoria='widebody', marca__icontains=q)
    return render(request, 'products/widebody.html', {'products': products})

