from django.shortcuts import render, redirect
from django.http import HttpResponse
from listings.models import band , band_title, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail

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

def listings_list(request):
    listings = Listing.objects.all()
    return render(request,'listings/listing_list.html',{'listings':listings})
    
    
def listing_detail(request, id):
    listings = Listing.objects.get(id=id)
    return render(request, 'listings/listing_detail.html', {'listings':listings})

def contact(request):
    if request.method == 'POST':
        #create an instance form and fill it with the post data
        form = ContactUsForm(request.POST)
        
        if form.is_valid():
            send_mail(subject=f'Message from {"name" or "anonymous"} via Merchex Contact us form',
                      message=form.cleaned_data['message'],
                      from_email=form.cleaned_data['email'],
                      recipient_list=['admin@merchex.xyz'],)
            return redirect('email-sent')
            #if the form is not valid, we let the execution continue to the return
            #statement below, and display the form again (with errors).
        
    else:
        # this must be a get request so create an empty form
        form = ContactUsForm()
    
    return render(request, 'listings/contact.html',{'form':form})
def emailSent(request):
    return render(request, 'listings/emailSent.html')
    
    
def create_band(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            #create a new band and save it to the db
            band = form.save()
            #REDIRECT to the detail page of the band we just created
            #we can provide the url pattern arguments as arguments to redirect function
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/create_band.html', {'form':form})
    
    
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
        
    else:
        form = ListingForm()
    return render(request, 'listings/create_listing.html', {'form':form})
def update_band(request,id):
    bands = band.objects.get(id=id)
    
    if request.method == 'POST':
        form = BandForm(request.POST,instance=bands)
        if form.is_valid():
            #update the existing band in the database
            form.save()
            #REDIRECT to the datapage of the form we just updated
            return redirect('band-detail', band.id)
        
    else:
        form = BandForm(instance=bands)
        
    return render(request, 'listings/update_band.html', {'form':form})

def update_listing(request,id):
    listings = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listings)
        if form.is_valid():
            form.save()
            return redirect('listing-detail', listings.id)
        
    else:
        form = ListingForm(instance=listings)
    return render(request, 'listings/update_listing.html', {'form':form})
def delete_band(request, id):
    bands = band.objects.get(id=id)
    if request.method == "POST":
        #delete the band from the database
        bands.delete()
        #redirect to the bands list
        return redirect('band-list')
    #no need for an 'else' here. if its a get request, just continue.
    return render(request, 'listings/delete_band.html', {'bands':bands})

def delete_listing(request,id):
    listings = Listing.objects.get(id=id)
    if request.method == "POST":
        listings.delete()
        return redirect('Listings-list')
    
    return render(request, 'listings/delete_listing.html', {'listings':listings})
    
    
