from django.contrib import admin

from .models.category import Category
from .models.sub_category import Sub_Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Sub_Category)
