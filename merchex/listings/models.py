from django.db import models

# Create your models here.


class band(models.Model):
    name = models.fields.CharField( max_length=100)
    
    
class band_title(models.Model):
    title = models.fields.CharField(max_length=100)
    
