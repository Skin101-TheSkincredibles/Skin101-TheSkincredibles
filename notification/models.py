from django.db import models


# Create your models here.
class Notification(models.Model):
    title = models.CharField(max_length=100)
    messages = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
