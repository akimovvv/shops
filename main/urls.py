from django.urls import path
from .views import *

urlpatterns = [
    path('product/<slug:product_slug>/', Product_detail_view.as_view(), name='productdetailview'),
    path('categories/<slug:slug>/', CategoriesView.as_view(), name='categoryview'),
    path('about/', about, name='about'),
    path('myprofile/', my_profile, name='myprofile'),
    path('editprofile/', edit_profile, name='editprofile'),
    path('singup/', singup, name='singup'),
    path('singin/', singin, name='singin'),
    path('logout/', user_logout, name='logout'),
    path('', BaseView.as_view(), name='main'),
]