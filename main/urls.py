from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('singup/', singup, name='singup'),
    path('singin/', singin, name='singin'),
    path('logout/', user_logout, name='logout')
]