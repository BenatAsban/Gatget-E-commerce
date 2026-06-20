import json
from django.shortcuts import render
from flask import redirect
from . models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def home(request):
    return render(request,"store/home/home.html") 
     

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You have been logged out!!')
    return redirect("/")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  # Authenticate the user
            messages.success(request, "Login Successfully")
            return redirect('/')  # Redirect to the home page
        else:
            messages.error(request, "Invalid username or password")
            return redirect('/')  # Redirect back to the login page in case of failed login
    else:
        return render(request, "store/login/login.html")    
    
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        try:
            user = User.objects.create_user(username=name, email=email, password=password1)
            messages.success(request, "Registration Success. You can login now.")
            return redirect('login')  # Redirect to the login page after successful registration
        except Exception as e:
            messages.error(request, "Error occurred")
            return redirect('register')

    return render(request, "store/register/register.html")

def categories(request):
    category=Category.objects.filter(status=0)
    return render(request,"store/categories/categories.html",{"category":category})

def productsview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)
        return render(request,"store/products/products.html",{"products":products,"category_name":name})
    else:
       messages.warning(request,"No Such Category Found")
       return redirect('categories')
   
   
def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
      if(Product.objects.filter(name=pname,status=0)):
        products=Product.objects.filter(name=pname,status=0).first()
        return render(request,"store/product_details/product_details.html",{"products":products})
      else:
        messages.warning(request,"No Such Products Found")
        return redirect('categories')
    else:
        messages.warning(request,"No Such Category Found")
        return redirect("categories")   
