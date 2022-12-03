from django import forms
from productdisplay.models import Tags

class QuizSession(forms.Form):

    # Apa produk yang kamu cari?
    Q1 = [
        ('cleanser','Pembersih/Cleanser'),
        ('moisturizer','Pelembab/Moisturizer'),
        ('sunscreen','Tabir Surya/Sunscreen'),
        ('toner','Toner'),
        ('serum','Serum'),
        ('misc','Produk Tambahan')
        ]
    type = forms.CharField(label='type', widget=forms.RadioSelect(choices=Q1))

    # Apa kulitmu berminyak?
    Q2 = [
        (True,'Iya'),
        (False,'Tidak')
        ]
    oily = forms.CharField(label='oily', widget=forms.RadioSelect(choices=Q2))

    # Apa kulitmu mudah merah atau sering iritasi?
    Q3 =[
        (True,'Iya'),
        (False,'Tidak')
        ]
    sensitive = forms.CharField(label='sensitive', widget=forms.RadioSelect(choices=Q3))

    # Apa kulitmu gampang berjerawat?
    Q4 = [
        (True,'Iya'),
        (False,'Tidak')
        ]
    acne = forms.CharField(label='acne', widget=forms.RadioSelect(choices=Q4))

    # Apakah kulitmu sering kering atau bersisik?
    Q5 = [
        (True,'Iya'),
        (False,'Tidak')
        ]
    dry = forms.CharField(label='dry', widget=forms.RadioSelect(choices=Q5))


NUMS= [
    ('one', 'one'),
    ('two', 'two'),
    ('three', 'three'),
    ('four', 'four'),
    ('five', 'fives'),

    ]

NOMS= [
    # kiri submit, kanan diform
    ('kiri1', 'kanan1'),
    ('kiri3', 'kanan3'),
    ('kiri5', 'kanan5'),
    ('kiri7', 'kanan7'),
    (Tags.objects.filter(name='oily'), 'kanan9'),

    ]

class CHOICES(forms.Form):
    NUMS = forms.CharField(widget=forms.RadioSelect(choices=NUMS))
    NOMS = forms.CharField(widget=forms.RadioSelect(choices=NOMS))

