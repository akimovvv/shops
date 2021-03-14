from django.shortcuts import render, redirect
from .forms import Register, Login
from django.contrib.auth import login, logout

# Create your views here.
def index(request):
    return render(request, 'main/base.html')

def singup(requset):
    if requset.method == 'POST':
        form = Register(requset.POST)
        if form.is_valid():
            form.save()
            return redirect('singin')
    else:
        form = Register()
        return render(requset, 'main/registrate.html', {'form': form})

def singin(request):
    if request.method == 'POST':
        form = Login(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = Login()
        return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')
