from django.db import models

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=50)

class SkinCareItem(models.Model):

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50) 
    tags = models.ManyToManyField(Tags)
    price = models.CharField(max_length=50)

class Display(models.Model):
    list_of_mosturizer = models.ManyToManyField(SkinCareItem)
    list_of_sunscreen = models.ManyToManyField(SkinCareItem)
    list_of_serum = models.ManyToManyField(SkinCareItem)
    list_of_facewash = models.ManyToManyField(SkinCareItem)
    list_of_toner = models.ManyToManyField(SkinCareItem)
    list_of_misc = models.ManyToManyField(SkinCareItem)
    list_of_tags = models.ManyToManyField(SkinCareItem)