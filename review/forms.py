from django.forms import ModelForm
from .models import ReviewModel
from django import forms

class ReviewForm(ModelForm):
    class Meta:
        model = ReviewModel
        fields = ['username', 'nama_produk', 'tipe', 'isi_review']
