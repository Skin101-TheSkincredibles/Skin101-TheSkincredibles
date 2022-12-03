from django.urls import path
from .views import *

urlpatterns = [
    #path('', daftar_artikel, name='daftar_artikel'),
    path('recommendation/', generate_recommendation, name='recommendation'),
    path('tes/', test, name='tes'),
    path('',start_session,name='start_session')
]