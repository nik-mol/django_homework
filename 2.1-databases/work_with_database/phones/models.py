from email.policy import default
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import BooleanField, DateField, SlugField


class Phone(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)

    def __str__(self) -> str:
        return f'{self.name}'

    

