from django.urls import path
from .views import set_notification, get_notification, fetch_notification_datas

urlpatterns = [
    path('set-notification', set_notification, name='set-notification'),
    path('get-notification', get_notification, name='get-notification'),
    path('notification-datas', fetch_notification_datas, name='notification-datas'),
    # path('notif-data', notif_data, name='notif-data')
]