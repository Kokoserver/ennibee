from django.contrib import admin

from store.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_available", "updated_at", "created_at")
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Product, ProductAdmin)
