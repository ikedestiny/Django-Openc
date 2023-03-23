from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class band(models.Model):
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP ='SP'
        ALTERNATIVE_ROCK = 'AR'
        AFROPOP = 'AP'
        AFROFUSION = 'AF'
        BLUES = 'BL'
        COUNTRY = 'CT'
        JAZZ = 'JZ'
        
    name = models.fields.CharField( max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=150)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)],default=2000
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
   
    def __str__(self):
        return f'{self.name}'
    
class band_title(models.Model):
    title = models.fields.CharField(max_length=100)
    
class Listing(models.Model):
    class Type(models.TextChoices):
        RECORDS = 'RC'
        CLOTHING = 'CL'
        POSTERS = 'PT'
        MISCELLANEOUS = 'MC'
    description = models.fields.CharField(max_length=150)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)],null=True)
    type = models.fields.CharField(choices=Type.choices, max_length=50)   
    
    def __str__(self):
        return f'{self.type}' 
    Band = models.ForeignKey(band, null=True, on_delete=models.SET_NULL)
      
