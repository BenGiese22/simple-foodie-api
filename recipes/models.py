import datetime
from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    link = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    directions = models.CharField(max_length=2000)
    source = models.CharField(max_length=50)
    created_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.created_date >= timezone.now() - datetime.timedelta(days=1)
        