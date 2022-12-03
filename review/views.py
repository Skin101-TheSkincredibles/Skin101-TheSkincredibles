from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from review import models
from .serializers import reviewSerializers

# Create your views here.
class listReview(generics.ListCreateAPIView):
    queryset = models.ReviewModel.objects.all().order_by('-date_created')
    serializer_class = reviewSerializers

class detailReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ReviewModel.objects.all()
    serializer_class = reviewSerializers

def index(request):
    review = ReviewModel.objects.all().order_by('-date_created')
    context = {'review':review}
    return render(request, 'all_reviews.html', context)

def create_review(request):
    form = ReviewForm(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            instance = form.save()
            instance.save()
            return redirect('/review')

    context = {'form':form}
    return render(request, 'create_review.html', context)

def review_detail(request, pk):
    review = ReviewModel.objects.get(id=pk)
    return render(request, 'review_detail.html', {'review': review})