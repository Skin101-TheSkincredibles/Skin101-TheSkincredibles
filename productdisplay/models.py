from django.db import models

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SkinCareItem(models.Model):

    name = models.CharField(max_length=200)
    type = models.CharField(max_length=50) 
    tags = models.ManyToManyField(Tags)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.name

