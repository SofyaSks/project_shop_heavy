from django.contrib import admin
from . models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    # значения, которые заполняются автоматически
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated', 'discount']
    # то, по чему будет фильтрация
    list_filter = ['available', 'created', 'updated']
    # то , что можем изменить после создания
    list_editable = ['price', 'available', 'discount']
    prepopulated_fields = {'slug': ('name', )}
    
