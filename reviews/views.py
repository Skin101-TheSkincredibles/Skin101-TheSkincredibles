from django.shortcuts import render, redirect
from reviews import models
from reviews.models import ReviewsModel
from reviews.forms import ReviewForm
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from reviews.serializers import reviewSerializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from reviews.filters import * 
from django.contrib.auth import get_user

# Create your views here.
class listReview(generics.ListCreateAPIView):
    queryset = models.ReviewsModel.objects.all().order_by('-date_created')
    serializer_class = reviewSerializers

class detailReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ReviewsModel.objects.all()
    serializer_class = reviewSerializers

@login_required(login_url='login')
def index(request):
    review = ReviewsModel.objects.all().order_by('-date_created')
    myFilter = ProductFilter(request.GET, queryset=review)
    review = myFilter.qs
    context = {'myFilter':myFilter, 'review':review}
    return render(request, 'all_reviews.html', context)

@login_required(login_url='login')
def create_review(request):
    print("mulai")
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        print("harusnya kebuat")
        if form.is_valid():
            instance = form.save()
            instance.save()
            print("dah kesave")
            return redirect('/reviews')
    else:
        user = get_user(request)
        form = ReviewForm(initial={'username': user})
    print("yah")

    context = {'form':form}
    return render(request, 'create_review.html', context)

@login_required(login_url='login')
def review_detail(request, pk):
    review = ReviewsModel.objects.get(id=pk)
    total_likes = review.number_of_likes()
    context = {'review':review, 'total_likes':total_likes}

    return render(request, 'review_detail.html', context)

@login_required(login_url='login')
def LikeView(request, pk):
    review = get_object_or_404(ReviewsModel, id=request.POST.get('review_id'))
    if review.likes.filter(id=request.user.id).exists():
        review.likes.remove(request.user)
    else:
        review.likes.add(request.user)

    return HttpResponseRedirect(reverse('review_detail', args=[str(pk)]))