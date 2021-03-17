from django.shortcuts import render, redirect
from .forms import Register, Login, UserEdit
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.views.generic.base import View
from django.contrib import messages
from .models import *



class BaseView(View):
    def get(self, request):
        categories = Category.objects.all()
        products = Product.objects.all()
        context = {'categories_list': categories, 'products_list': products}
        return render(request, 'main/base.html', context)



class CategoriesView(View):
    def get(self, request, slug):
        products = Product.objects.filter(category__slug=slug)
        context = {'products_list': products}
        return render(request, 'main/product_view.html', context)



class Product_detail_view(View):
    def get(self, request, product_slug):
        product = Product.objects.get(slug=product_slug)
        context = {'product': product}
        return render(request, 'main/product_detail_view.html', context)



def my_profile(request):
    return render(request, 'main/profile.html')



def about(request):
    return render(request, 'main/about.html')



def singup(request):
    if request.method == 'POST':
        form = Register(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your registrated success!')
            return redirect('singin')
        else:
            messages.error(request, 'Registration error!')
    else:
        form = Register()
    return render(request, 'main/registrate.html', {'form': form})



def singin(request):
    if request.method == 'POST':
        form = Login(data=request.POST or None)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Your sing in success!')
            return redirect('/')
        else:
            messages.error(request, 'Sing in error!')
    else:
        form = Login()
    return render(request, 'main/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('/')



def edit_profile(request):
    if request.method == 'POST':
        form = UserEdit(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data.get('username')
            new_first_name = form.cleaned_data.get('first_name')
            new_email = form.cleaned_data.get('email')
            # old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            user = User.objects.get(username=request.user.username)
            if new_username:
                user.username = new_username
            if new_first_name:
                user.first_name = new_first_name
            if new_email:
                user.email = new_email
            if new_password:
                user.set_password(new_password)
            user.save()
            messages.success(request, 'You edit profile success!')
            return redirect('/')
        else:
            messages.error(request, 'Edit error!')
    else:
        form = UserEdit()
    return render(request, 'main/edit_profile.html', {'form': form})