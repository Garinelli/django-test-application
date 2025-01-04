from django.shortcuts import render
from .forms import RegisterForm, LoginForm

def index_page(request):
    return render(request, 'index.html')


def register_page(request):
    form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_page(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})