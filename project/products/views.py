from django.shortcuts import render
from .models import Productos

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

from django.shortcuts import render


def llantas(request):
    q = request.GET.get('q', '')
    products = Productos.objects.filter(category='llantas', name__icontains=q)
    return render(request, 'products/llantas.html', {'products': products})

def llantas(request):
    q = request.GET.get('q', '')
    products = Productos.objects.filter(category='alerones', name__icontains=q)
    return render(request, 'products/alerones.html', {'products': products})

def llantas(request):
    q = request.GET.get('q', '')
    products = Productos.objects.filter(category='spoilers', name__icontains=q)
    return render(request, 'products/spoilers.html', {'products': products})

def llantas(request):
    q = request.GET.get('q', '')
    products = Productos.objects.filter(category='intakes', name__icontains=q)
    return render(request, 'products/intakes.html', {'products': products})

def llantas(request):
    q = request.GET.get('q', '')
    products = Productos.objects.filter(category='widebody', name__icontains=q)
    return render(request, 'products/widebody.html', {'products': products})

