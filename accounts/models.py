from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, blank=True)
    nickname = models.CharField(max_length=20, blank=True)
    birthday = models.DateField(null=True, blank=True)
    phoneNumber = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.nickname
