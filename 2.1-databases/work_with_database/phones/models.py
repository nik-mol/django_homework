from unittest.util import _MAX_LENGTH
from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
