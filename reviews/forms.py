from django.forms import ModelForm
from reviews.models import ReviewsModel
from django import forms

class ReviewForm(ModelForm):
    class Meta:
        model = ReviewsModel
        fields = ['username','nama_produk', 'tipe', 'isi_review', 'image']