from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class Register(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')



class Login(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class UserEdit(forms.Form):
    username = forms.CharField(required=False, label='Edit username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=False, label='Edit first name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=False, label='Edit email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # old_password = forms.CharField(required=False, label='Old password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(required=False, label='New password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))