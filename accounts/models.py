from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=500, blank=True)
    number = models.TextField(max_length=10)
    city = models.TextField(max_length=20)
    state = models.TextField(max_length=20)
    zipcode = models.TextField(max_length=10)

    def __str__(self):
        return self.user.username

