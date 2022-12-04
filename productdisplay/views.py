from django.shortcuts import render
from productdisplay.models import SkinCareItem
# Create your views here.

def get_products(): #get all products
    return SkinCareItem.objects.all()

def filter_by(tags): #filter by tags
    all_products = get_products()
    return all_products.filter(tags__pk__in=tags)

def show_all_products(request): #show all products in html
    context = {'products':get_products()}
    return render(request, 'index.html', context)

def show_filtered_products(request): #show filtered contents in html
        #TES aja dibawah
    type = request.session.get('type')
    tags = request.session.get('tags')
    res = filter_by(tags).distinct().filter(type=type)
    context = {'products':res}
    return render(request, 'index.html', context)

def show_product_detail(request, product_id): #show detailed information about a skincare once a client click on their respective button.
    sc = SkinCareItem.objects.get(pk=product_id)
    context = {'product':sc}
    return render(request, 'detail.html', context)
    
