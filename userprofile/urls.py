from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='user-profile'),
    path('edit-profile/', views.profileupdate, name='update-profile'), 
    path('profile/profile-datas/', views.profiledatas, name='profile-datas'),
]