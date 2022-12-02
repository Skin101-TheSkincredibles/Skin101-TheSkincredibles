from django import forms

class QuizSession(forms.Form):

    # Apa produk yang kamu cari?
    Q1 = [('Pembersih/Cleanser'),('Pelembab/Moisturizer'),('Tabir Surya/Sunscreen'),('Produk tambahan')]
    type = forms.CharField(label='type', widget=forms.RadioSelect(choices=Q1))

    # Apa kulitmu berminyak?
    Q2 = [('Iya'),('Tidak')]
    oily = forms.CharField(label='oily', widget=forms.RadioSelect(choices=Q2))

    # Apa kulitmu mudah merah atau sering iritasi?
    Q3 = [('Iya'),('Tidak')]
    sensitive = forms.CharField(label='sensitive', widget=forms.RadioSelect(choices=Q3))

    # Apa kulitmu gampang berjerawat?
    Q4 = [('Iya'),('Tidak')]
    acne = forms.CharField(label='acne', widget=forms.RadioSelect(choices=Q4))

    # Apakah kulitmu sering kering atau bersisik?
    Q5 = [('Iya'),('Tidak')]
    dry = forms.CharField(label='dry', widget=forms.RadioSelect(choices=Q5))

    # isu : gatau cara ambil jawabannya huwuw

