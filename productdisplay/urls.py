from . import views
from django.urls import path
urlpatterns = [
    path('', views.show_all_products, name='index'),
    path('filtered/', views.show_filtered_products, name='filtered_products')
]