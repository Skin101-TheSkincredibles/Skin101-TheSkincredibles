from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_cas_ng.signals import cas_user_authenticated
import json

# Create your models here.
@receiver(cas_user_authenticated)
def save_cas_user_attributes(user, attributes, **kwargs):
  """Save attributes for user that authenticated from CAS"""

  full_name = attributes.get('nama', '').split()
  user.first_name = full_name[0]
  user.last_name = full_name[-1]
  user.profile.name = attributes.get('nama', '')
  user.save()