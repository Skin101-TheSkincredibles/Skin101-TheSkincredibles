from django.urls import path
from .views import start_session,generate_recommendation

urlpatterns = [
    #path('', daftar_artikel, name='daftar_artikel'),
    path('', start_session, name='start_session'),
    path('recommendation/', generate_recommendation, name='recommendation')
]