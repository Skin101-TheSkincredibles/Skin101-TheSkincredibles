from django import forms
from django.forms import ModelForm
from .models import Notification as NotificationModel


class NotificationForm(ModelForm):
    class Meta:
        model = NotificationModel
        fields = ['title', 'messages']
