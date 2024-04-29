from django.contrib import admin

from .models import Category, Product

# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
    list_display = ('name', 'price', 'image')
    list_filter = ('created',)
    search_fields = ('name',)