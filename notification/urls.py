from django.urls import path
from .views import make_notification, get_notification

urlpatterns = [
    path('make-notification', make_notification, name='ake-notification'),
    path('get-notification', get_notification, name='get-notification'),
]