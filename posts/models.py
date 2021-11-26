
from django.db import models
from django.db.models.aggregates import Max

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    age = models.PositiveIntegerField()