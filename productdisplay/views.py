from django.shortcuts import render
from productdisplay.models import Tags, SkinCareItem
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
    context = {'products':get_products()}
    return render(request, 'index.html', context)