from django import views
from django.shortcuts import render
from django.views import View
from Shop.models.category import Category



# Create your views here.


class Index(views.View):
    def get(self,request):

        category=Category.objects.all()
        data={}
        data['category']=category
        return render(request,"index.html",data)