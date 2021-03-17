from django.urls import path
from .views import *

urlpatterns = [
    # path('categories/<slug:slug_1>/<slug:slug_2>/', MakerView.as_view(), name='makerview'),
    path('categories/<slug:slug>/', CategoriesView.as_view(), name='categoryview'),
    path('about/', about, name='about'),
    path('myprofile/', my_profile, name='myprofile'),
    path('editprofile/', edit_profile, name='editprofile'),
    path('singup/', singup, name='singup'),
    path('singin/', singin, name='singin'),
    path('logout/', user_logout, name='logout'),
    path('', BaseView.as_view(), name='main'),
]