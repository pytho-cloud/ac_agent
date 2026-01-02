from django.contrib import admin

# Register your models here.
from .models import AC

@admin.register(AC)
class ACAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model_name', 'condition', 'ac_type', 'capacity', 'energy_rating', 'price', 'is_available')
    list_filter = ('condition', 'ac_type', 'brand', 'energy_rating')
    search_fields = ('brand', 'model_name')