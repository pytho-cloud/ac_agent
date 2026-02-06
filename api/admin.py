from django.contrib import admin

# Register your models here.
from .models import *

# @admin.register(AC)
# class ACAdmin(admin.ModelAdmin):
#     list_display = (
#         'brand', 'model_name', 'ac_types',
#         'capacity', 'energy_rating', 'price',
#         'is_available', 'is_home_active'
#     )

class ACImageInline(admin.TabularInline):
    model = ACImage
    extra = 3

@admin.register(AC)
class ACAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'model_name',
        'ac_types_display',  # custom display method
        'capacity',
        'energy_rating',
        'price',
        'is_available',
        'is_home_active',
    )

    def ac_types_display(self, obj):
        # Convert list to string
        return ", ".join(obj.ac_types) if obj.ac_types else "-"
    
    ac_types_display.short_description = "AC Types"
# @admin.register(Review)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'product_name',
#         'star',
#         'phone_number',
#         'email',
#         'created_at',
#     )
#     list_filter = ('star', 'product_name')
#     search_fields = ('name', 'product_name', 'email', 'phone_number')
#     ordering = ('-created_at',)








@admin.register(Maintainence)
class MaintainenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'is_active')  # Update to match current model fields
    list_filter = ('is_active',)
    search_fields = ('title', 'description')

@admin.register(Reviews)
class Reviews(admin.ModelAdmin):

    list_display =(
        'name',
        'product_name' ,
        'review',
        'rating',
        'is_active'
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


# @admin.register(ProductSell)
# class ProductSellAdmin(admin.ModelAdmin):
#     list_display = ('name' , 'address', 'product_name' , 'phone_number','created_at')
    

class ProductSellImagesInline(admin.TabularInline):
    model = ProductSellImages
    extra = 1


@admin.register(ProductSell)
class ProductSellAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "product_name", "phone_number", "price", "created_at")
    search_fields = ("name", "product_name", "phone_number")
    list_filter = ("created_at",)
    inlines = [ProductSellImagesInline]


@admin.register(ServiceEnquiry)
class ServiceEnquiryAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "email", "created_at")
