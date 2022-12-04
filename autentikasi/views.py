from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt

from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from notification.models import Notification


@csrf_exempt
def home(request):
    if request.user.is_authenticated:
        form = (Notification.objects.all().values()).last()
        context = {'form': form}
        return render(request, 'autentikasi/home.html', context)
    else:
        return render(request, 'autentikasi/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'autentikasi/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'autentikasi/profile.html')
