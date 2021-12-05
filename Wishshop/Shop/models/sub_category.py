from django.db import models
from django.db.models.base import Model
from .category import Category

class Sub_Category(models.Model):
    
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=300)

    def __str__(self):
        return self.name
        

