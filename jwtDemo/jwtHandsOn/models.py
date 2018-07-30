# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.contrib.auth.models import AbstractUser
from pytz import timezone
from django.db import models


class User(AbstractUser):
    username = models.CharField(unique=True,max_length=40)
    email = models.EmailField(
        unique=True,
        max_length=254,
    )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    mobile = models.IntegerField(unique=True)
    # date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)