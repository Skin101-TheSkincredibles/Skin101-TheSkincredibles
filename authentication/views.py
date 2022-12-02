from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_protect
from .models import User
from .forms import LoginForm, SignupForm
from .utils import request_schema
from . import schema as schema


def index(request):
  prop = {
    'type': 'login',
    'form': LoginForm(),
  }
  return render(request, 'index.html', prop)

def loginView(request):
  if(request.user.is_authenticated):
    return redirect('/home')

  return index(request)

def signupView(request):
  if(request.user.is_authenticated):
    return redirect('/')

  return index(request)

def logoutView(request):
  logout(request)
  return redirect('/auth/login/')


@csrf_protect
@request_schema(method='POST', schema=schema.login_api_request)
def loginApi(request, data):
  if request.is_ajax:
    user = authenticate(username=data['username'], password=data['password'])

    if user is not None:
      login(request, user)
      return JsonResponse(status=200, data={'message': 'Login Success'})
    else:
      if User.objects.filter(username=data['username']).count():
        return JsonResponse(status=400, data={'message': 'The username and password does\'nt match!'})
      else:
        return JsonResponse(status=400, data={'message': 'There are no user with the given username!'})

  return JsonResponse(status=500, data={'message': 'Internal Server Error'})

@csrf_protect
@request_schema(method='POST', schema=schema.signup_api_request)
def signupApi(request, data):
  if request.is_ajax:
    form = UserCreationForm(data)

    if form.is_valid():
      form.save()
      new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
      login(request, new_user)
      return JsonResponse(status=200, data={"message": "User registration successful", "username": form.cleaned_data['username']})
    else:
      return JsonResponse(status=400, data={"message": "User registration failed", "error": form.errors})

  return JsonResponse(status=500, data={'message': 'Internal Server Error'})