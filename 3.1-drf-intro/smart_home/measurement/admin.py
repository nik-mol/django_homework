from django.contrib import admin

from .models import Measurement, Sensor

# Register your models here.

@admin.register(Sensor)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')

@admin.register(Measurement)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'temperature', 'created_at', 'image')
    list_display_links = ('id',)

