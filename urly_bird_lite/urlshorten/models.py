from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class URL(models.Model):
    author = models.ForeignKey(User)
    url = models.URLField(max_length=100)
    shortened_url = models.CharField(max_length=50)
    time = models.DateTimeField(default=datetime.datetime.now)
    description = models.TextField()

    class Meta:
        ordering = ['-time']




