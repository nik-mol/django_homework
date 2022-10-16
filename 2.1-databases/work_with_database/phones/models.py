from django.db import models
from django_extensions.db.fields import AutoSlugField

# from django.forms import BooleanField, DateField, SlugField


class Phone(models.Model):
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=1)
    image = models.CharField(max_length=100)
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True)
  
    

