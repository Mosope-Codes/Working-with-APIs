from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(blank=True, unique=True)
    author = get_user_model()
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)
