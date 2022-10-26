from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class House(models.Model):

    # Model definition for Houses

    name = models.CharField(max_length=140)
    price = models.PositiveBigIntegerField()
    description = models.TextField()
    adress = models.CharField(max_length=140)