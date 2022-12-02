from django.urls import path
from .views import start_session

urlpatterns = [
    #path('', daftar_artikel, name='daftar_artikel'),
    path('start/', start_session, name='start_session')
]