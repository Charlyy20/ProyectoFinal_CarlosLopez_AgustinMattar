from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')

def portfolio_details(request):
    return render(request, 'core/portfolio-details.html')