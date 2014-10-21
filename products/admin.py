from django.contrib import admin

from models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'delivery', 'free_porto', 'kids', 'kid_adult',
                    'women', 'package')
    list_filter = ('delivery', 'free_porto', 'kids', 'kid_adult', 'women',
                   'package')


admin.site.register(Product, ProductAdmin)
