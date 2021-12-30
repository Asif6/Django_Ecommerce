from django import views
from django.shortcuts import render
from django.views import View
from Shop.models.category import Category
from Shop.models.products import Product



# Create your views here.


class Index(views.View):
    def get(self,request):

        category_id=request.GET.get("category")
        category=Category.objects.all()
        b_category=request.GET.get("b_category")

        b_product=Product.objects.filter(category_id=b_category)

        if category_id:
            products=Product.objects.filter(sub_category_id=category_id).order_by("-id")
        else:
            products=Product.objects.all().order_by("-id")
        data={}
        data['category']=category
        data['product']=products
        data['b_product']=b_product
        return render(request,"index.html",data)