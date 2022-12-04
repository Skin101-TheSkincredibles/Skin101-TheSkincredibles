from django import forms
from productdisplay.models import Tags

class QuizSession(forms.Form):


    Q1 = [
        ('cleanser','Pembersih/Cleanser'),
        ('moisturizer','Pelembab/Moisturizer'),
        ('sunscreen','Tabir Surya/Sunscreen'),
        ('toner','Toner'),
        ('serum','Serum'),
        ('misc','Produk Tambahan')
        ]
    type = forms.CharField(label='type', widget=forms.RadioSelect(choices=Q1))

    Q2 = [
        (True,'Iya'),
        (False,'Tidak')
        ]

    oily = forms.CharField(label='oily', widget=forms.RadioSelect(choices=Q2))

    sensitive = forms.CharField(label='sensitive', widget=forms.RadioSelect(choices=Q2))

    acne = forms.CharField(label='acne', widget=forms.RadioSelect(choices=Q2))

    dry = forms.CharField(label='dry', widget=forms.RadioSelect(choices=Q2))
