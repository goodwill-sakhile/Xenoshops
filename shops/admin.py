from django.contrib import admin
from .models import Shop

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'address', 'phone_number', 'created_at')
    search_fields = ('name', 'category', 'address')
