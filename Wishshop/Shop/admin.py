from django.contrib import admin

from .models.category import Category
from .models.sub_category import Sub_Category
from .models.products import Product

# Register your models here.

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
