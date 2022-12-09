from django.shortcuts import render
from productdisplay.models import SkinCareItem, Tags
from productdisplay.forms import FilterForm
from django.contrib import messages
# Create your views here.

def getPks(form):
    pk_array = []
    isOily = form.cleaned_data['isOily']
    isSensitive= form.cleaned_data['isSensitive']
    isAcne = form.cleaned_data['isAcne']
    isDry = form.cleaned_data['isDry']
    isNormal = form.cleaned_data['isNormal']
   

    if(isOily):
        pk_array.append(1)
    if(isSensitive):
        pk_array.append(2)
    if(isAcne):
        pk_array.append(3)
    if(isDry):
        pk_array.append(4)
    if(isNormal):
        pk_array.append(5)

    return pk_array




def get_products(): #get all products
    return SkinCareItem.objects.all()

def filter_by(tags): #filter by tags
    all_products = get_products()
    return all_products.filter(tags__pk__in=tags)

def show_all_products(request): #show all products in html
  
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            tags = getPks(form)

            res = filter_by(tags).distinct().filter(type=type)
            context = {'products':res, 'form':form}
            return render(request, 'index.html', context)

    else:
        form = FilterForm()

    context = {'products':get_products(), 'form':form}
    return render(request, 'index.html', context)


def show_generated_products(request): #show filtered contents in html
        #TES aja dibawah
    type = request.session.get('type')
    tags = request.session.get('tags')
    form = FilterForm(request.POST)
    res = filter_by(tags).distinct().filter(type=type)
    context = {'products':res, 'form':form}
    return render(request, 'index.html', context)
