from django.shortcuts import render
from django.http import HttpResponse
from listings.models import band , band_title

def Hello(request):
    bands = band.objects.all()
    titles = band_title.objects.all()
    return render(request,'listings/hello.html',{'bands':bands})

def about(request):
    return HttpResponse('<h1>About-us</h1>  <p>We Love Merch!!</p>')

def goods(request):
    return HttpResponse("<p>That’s a great question.  Django takes care of the rest.</p>")
