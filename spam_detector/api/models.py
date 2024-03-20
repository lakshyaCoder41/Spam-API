from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    password=models.CharField(max_length=250, unique=True,null=False,default='dummy_password')
    email = models.EmailField(blank=True, null=True)
    username=models.CharField(max_length=20,unique=True,default='dummy_user')

    def __str__(self):
        return self.username

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    number = models.CharField(max_length=15, unique=True)
    is_spam = models.BooleanField(default=False)
    owner_name = models.CharField(max_length=255, blank=True, null=True)
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.number


