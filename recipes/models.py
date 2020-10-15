import datetime
from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    link = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=3000)
    directions = models.CharField(max_length=4000)
    source = models.CharField(max_length=50)
    created_date = models.DateTimeField('date published')
    image = models.CharField(max_length=5000, blank=True)
    total_prep_time = models.IntegerField(blank=True, null=True)