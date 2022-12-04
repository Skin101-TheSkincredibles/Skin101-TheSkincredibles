from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from review import models
from .serializers import reviewSerializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .filters import * 

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
    total_likes = review.number_of_likes()
    context = {'review':review, 'total_likes':total_likes}

    return render(request, 'review_detail.html', context)

def LikeView(request, pk):
    review = get_object_or_404(ReviewModel, id=request.POST.get('review_id'))
    if review.likes.filter(id=request.user.id).exists():
        review.likes.remove(request.user)
    else:
        review.likes.add(request.user)

    return HttpResponseRedirect(reverse('review_detail', args=[str(pk)]))

def search_reviews(request):
	if request.method == "POST":
		searched = request.POST['searched']
		review = ReviewModel.objects.filter(name__contains=searched)
	
		return render(request, 
		'all_reviews.html', 
		{'searched':searched,
		'review':review})
	else:
		return render(request, 
		'all_reviews.html', 
		{})