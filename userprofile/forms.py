from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import widgets
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__' #show all
        exclude = ['user',]