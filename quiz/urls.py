from django.urls import path
from .views import *

urlpatterns = [
    path('',start_session,name='start_session')
]