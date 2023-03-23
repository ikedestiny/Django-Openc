from django.shortcuts import render
from django.http import HttpResponse
from listings.models import band , band_title

def band_list(request):
    bands = band.objects.all()
    
    return render(request,'listings/band_list.html',{'bands':bands})

def band_detail(request, id):
    bands = band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'bands':bands})

def about(request):
    return render(request, 'listings/about.html')

def goods(request):
    titles = band_title.objects.all()
    return render(request,'listings/goods.html',{'titles':titles})

def products(request):
    return render(request, 'listings/products.html')
