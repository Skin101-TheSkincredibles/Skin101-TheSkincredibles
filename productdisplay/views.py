from django.shortcuts import render
from django.http import HttpResponse
from productdisplay.models import Tags, SkinCareItem
import sqlite3
# Create your views here.

def get_products(): #get all products
    return SkinCareItem.objects.all()

def filter_by(tags):
    all_products = get_products()
    return all_products.filter(tags__pk__in=tags)

def index(request):
    #TES aja dibawah
    res = filter_by([2,4]).distinct()
    print(res)
    return HttpResponse("Hello, world. You're at the polls index.")