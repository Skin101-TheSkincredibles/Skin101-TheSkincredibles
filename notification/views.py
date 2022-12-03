from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Notification
from .forms import NotificationForm
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser)
def make_notification(request):
    form = NotificationForm(request.POST or None)

    if (request.method == 'POST'):
        if (form.is_valid):
            form.save()

            return HttpResponseRedirect("/notification/")

    response = {'form': form}
    return render(request, 'make_notification.html', response)


@user_passes_test(lambda u: u.is_superuser)
def get_notification(request):
    announcement = Notification.objects.all()

    data = serializers.serialize('json', announcement)
    return HttpResponse(data, content_type="application/json")


from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
