import django_filters
from .models import *

class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = ReviewModel
        fields = {
            'nama_produk' : ['icontains']
        }