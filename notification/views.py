from django.shortcuts import redirect, render
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Notification
from .forms import NotificationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@user_passes_test(lambda u: u.is_superuser)
def get_notification(request):
    form = NotificationForm(request.POST)
    if (request.method == 'POST'):
        if (form.is_valid()):
            notif = Notification(title="title", messages="messages")
            notif.save()
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} has been made a notification for user!')
            print('balalalalal')
            return redirect('/administrator/')
    response = {'form': form}
    return render(request, 'set_notification.html', response)

# pake ini
@user_passes_test(lambda u: u.is_superuser)
def set_notification(request):
    form = NotificationForm(request.POST)
    if (request.method == 'POST'):
        print(form['title'].value())
        print(form['messages'].value())
        if (form.is_valid()):
            notif = Notification(title="title", messages="messages")
            notif.save()
            form.save()
            notif_data = {}
            notif_data['title'] = request.POST.get('title')
            notif_data['messages'] = request.POST.get('messages')
            print("OKEEE")
            return JsonResponse(notif_data, safe=False)
        print('bener kok post')
        return redirect('../home')
    elif (request.method == 'GET'):
        print('ini get bukan post')
    else:
        print('failed to post data')

    context = {
        'form': form,
    }
    return render(request, 'set_notification.html', context)



# @user_passes_test(lambda u: u.is_superuser)
@login_required
def fetch_notification_datas(request):
    form = Notification.objects.all().values()
    datas = serializers.serialize('json', form)
    print("datas: " + datas)
    response = {'form': form}
    return render(request, 'navbar_user.html', response)
    # return HttpResponse(response, content_type='application/json')

def notif_data(request):
    form = Notification.objects.all()
    data = serializers.serialize('json', form)
    print(form)
    print(data)
    return HttpResponse(data, content_type="applications/json")

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
