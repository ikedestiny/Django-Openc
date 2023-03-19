from django.contrib import admin

from listings.models import band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display=('name', 'year_formed', 'genre')

class ListingAdmin(admin.ModelAdmin):
    list_display=('description','type','year','sold')
    

admin.site.register(band, BandAdmin)
admin.site.register(Listing, ListingAdmin)