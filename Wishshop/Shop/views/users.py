from django import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout,login
from django.db import models
from django.views import View
from django.shortcuts import render , redirect


class Signup(views.View):

    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):

        username=request.POST.get('username')
        email=request.POST.get('email')
        first_name= request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        Password=request.POST.get('password')
     
        errormassage=None

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            errormassage='This Email or username All rady taken '
            return render(request,'signup.html',{"error":errormassage})
        else:
            user=User.objects.create_user(username=username,email=email, password=Password,first_name=first_name,last_name=last_name)
            user.save()
            errormassage="Account created successfully "
            return render(request,'signup.html', {'error':errormassage})


class Login(views.View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):

        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            errormassage="Invalid user"
            return render(request,'login.html',{'error':errormassage})


class Logout(views.View):
    def get(self,request):
        logout(request)
        return redirect('index')