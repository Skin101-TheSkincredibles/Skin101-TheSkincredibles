import django_filters
from .models import ReviewsModel
from django_filters import CharFilter

class ProductFilter(django_filters.FilterSet):
    nama_produk = CharFilter(field_name='nama_produk', lookup_expr='icontains')
    class Meta:
        model = ReviewsModel
        fields = ['nama_produk']