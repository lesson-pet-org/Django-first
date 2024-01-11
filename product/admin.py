from django.contrib import admin

from .models import Product, ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'description', 'price', 'name'
    )
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)