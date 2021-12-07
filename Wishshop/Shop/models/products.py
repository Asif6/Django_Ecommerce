from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.query_utils import subclasses
from .category import Category
from .sub_category import Sub_Category

class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.ImageField(upload_to="product/image")
    date=models.DateField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=CASCADE)
    sub_category=models.ForeignKey(Sub_Category,on_delete=CASCADE)

    def __str__(self):
        return self.name