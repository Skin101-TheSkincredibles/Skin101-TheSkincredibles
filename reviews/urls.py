from django.contrib import admin
from django.urls import include, path
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name="review"),
    path('create_review/', views.create_review, name="create_review"),
    path('review_detail/<str:pk>/', views.review_detail, name="review_detail"),
    path('like/<str:pk>', views.LikeView, name = 'like_review'),
    #path('search_reviews', views.search_reviews, name='search_reviews'),
    path('', listReview.as_view()),
    path('<int:pk>', detailReview.as_view())
]