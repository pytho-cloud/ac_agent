from django.contrib import admin

# Register your models here.
from .models import AC ,Review

@admin.register(AC)
class ACAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model_name', 'condition', 'ac_type', 'capacity', 'energy_rating', 'price', 'is_available')
    list_filter = ('condition', 'ac_type', 'brand', 'energy_rating')
    search_fields = ('brand', 'model_name')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product_name',
        'star',
        'phone_number',
        'email',
        'created_at',
    )
    list_filter = ('star', 'product_name')
    search_fields = ('name', 'product_name', 'email', 'phone_number')
    ordering = ('-created_at',)