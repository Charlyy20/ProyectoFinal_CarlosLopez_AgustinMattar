from django.shortcuts import render
from .models import Llantas, Alerones, Spoilers, Intakes, Widebody

def llantas_view(request):
    return render(request, 'products/llantas.html')

def spoilers_view(request):
    return render(request, 'products/spoilers.html')

def alerones_view(request):
    return render(request, 'products/alerones.html')

def intakes_view(request):
    return render(request, 'products/intakes.html')

def widebody_view(request):
    return render(request, 'products/widebody.html')

#-----------------------------------------------------------------------------------#

def llantas(request):
    q = request.GET.get('q', '')
    products = Llantas.objects.all()
    print(products)
    return render(request, 'products/llantas.html', {'products': products})

#def llantas(request):
    q = request.GET.get('q', '')
    products = Alerones.objects.filter(categoria='alerones', marca__icontains=q)
    return render(request, 'products/alerones.html', {'products': products})

#def llantas(request):
    q = request.GET.get('q', '')
    products = Spoilers.objects.filter(categoria='spoilers', marca__icontains=q)
    return render(request, 'products/spoilers.html', {'products': products})

#def llantas(request):
    q = request.GET.get('q', '')
    products = Intakes.objects.filter(categoria='intakes', marca__icontains=q)
    return render(request, 'products/intakes.html', {'products': products})

#def llantas(request):
    q = request.GET.get('q', '')
    products = Widebody.objects.filter(categoria='widebody', marca__icontains=q)
    return render(request, 'products/widebody.html', {'products': products})

