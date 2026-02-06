from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *


# =========================
# AC & AC Images
# =========================

class ACImageInline(admin.TabularInline):
    model = ACImage
    extra = 3


@admin.register(AC)
class ACAdmin(ImportExportModelAdmin):
    list_display = (
        'brand',
        'model_name',
        'ac_types_display',
        'capacity',
        'energy_rating',
        'price',
        'is_available',
        'is_home_active',
    )
    inlines = [ACImageInline]

    def ac_types_display(self, obj):
        return ", ".join(obj.ac_types) if obj.ac_types else "-"

    ac_types_display.short_description = "AC Types"


# =========================
# Maintainence
# =========================

@admin.register(Maintainence)
class MaintainenceAdmin(ImportExportModelAdmin):
    list_display = ('title', 'icon', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')


# =========================
# Reviews
# =========================

@admin.register(Reviews)
class ReviewsAdmin(ImportExportModelAdmin):
    list_display = (
        'name',
        'product_name',
        'review',
        'rating',
        'is_active'
    )
    list_filter = ('rating', 'is_active')
    search_fields = ('name', 'product_name')


# =========================
# Contact
# =========================

@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    search_fields = ("name", "email", "phone")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


# =========================
# Product Sell & Images
# =========================

class ProductSellImagesInline(admin.TabularInline):
    model = ProductSellImages
    extra = 1


@admin.register(ProductSell)
class ProductSellAdmin(ImportExportModelAdmin):
    list_display = ("id", "name", "product_name", "phone_number", "price", "created_at")
    search_fields = ("name", "product_name", "phone_number")
    list_filter = ("created_at",)
    inlines = [ProductSellImagesInline]


# =========================
# Service Enquiry
# =========================

@admin.register(ServiceEnquiry)
class ServiceEnquiryAdmin(ImportExportModelAdmin):
    list_display = ("full_name", "phone_number", "email", "created_at")
    search_fields = ("full_name", "phone_number", "email")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
