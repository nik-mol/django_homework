from django.contrib import admin

from .models import Advertisement

@admin.register(Advertisement)
class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at', 'status', 'creator')

# Register your models here.
