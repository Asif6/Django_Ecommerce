from django import views
from django.shortcuts import render
from django.views import View
from Shop.models.category import Category
from Shop.models.products import Product



# Create your views here.


class Index(views.View):
    def get(self,request):

        category_id=request.GET.get("category")
        print("CATEGORYYYYYYYYYYYYYYYYYYYYYYYYYYY", category_id)
        category=Category.objects.all()

        if category_id:
            products=Product.objects.filter(sub_category_id=category_id)
        else:
            products=Product.objects.all().order_by("-id")
        data={}
        data['category']=category
        data['product']=products
        return render(request,"index.html",data)