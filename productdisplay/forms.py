from django import forms
from django.core.exceptions import ValidationError
class FilterForm(forms.Form):
    Q1 = [
        ('cleanser','Pembersih/Cleanser'),
        ('moisturizer','Pelembab/Moisturizer'),
        ('sunscreen','Tabir Surya/Sunscreen'),
        ('toner','Toner'),
        ('serum','Serum'),
        ('misc','Produk Tambahan')
        ]
    isOily = forms.BooleanField(required=False, label='Oily', widget=forms.CheckboxInput)
    isSensitive = forms.BooleanField(required=False, label='Sensitive', widget=forms.CheckboxInput)
    isAcne = forms.BooleanField(required=False, label='Acne', widget=forms.CheckboxInput)
    isDry = forms.BooleanField(required=False, label='Dry', widget=forms.CheckboxInput)
    isNormal = forms.BooleanField(required=False, label='Normal', widget=forms.CheckboxInput)
    type = forms.CharField(label='type', widget=forms.RadioSelect(choices=Q1))



    def clean(self):
        bool_arr = []
        true_total = 0
        cleaned_data = super().clean()
        oilyBool = cleaned_data.get("isOily")
        sensiBool = cleaned_data.get("isSensitive")
        acneBool =  cleaned_data.get("isAcne")
        dryBool = cleaned_data.get("isDry")
        normalBool = cleaned_data.get("isNormal")

        bool_arr.append(oilyBool)
        bool_arr.append(sensiBool)
        bool_arr.append(acneBool)
        bool_arr.append(dryBool)
        bool_arr.append(normalBool)

        for cntr in range(0,5):
            if(bool_arr[cntr]):
                true_total+=1
        
        if(true_total==0):
            print("hello")
            raise ValidationError(
                    "Please pick at least one tag."
                )

        if(normalBool and true_total>1):
            raise ValidationError(
                    "You can only pick normal without the other tags."
                )


        


