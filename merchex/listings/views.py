from django.shortcuts import render
from django.http import HttpResponse
from listings.models import band , band_title

def Hello(request):
    bands = band.objects.all()
    
    return render(request,'listings/hello.html',{'bands':bands})

def about(request):
    return render(request, 'listings/about.html')

def goods(request):
    titles = band_title.objects.all()
    return render(request,'listings/goods.html',{'titles':titles})

def products(request):
    return render(request, 'listings/products.html')
