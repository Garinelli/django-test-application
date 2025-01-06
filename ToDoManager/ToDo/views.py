from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import User

def index_page(request):
    return render(request, 'index.html')

def register_page(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password']
            )
            return redirect('login-page')


@login_required
def tasks_page(request):
    return render (request, 'tasks.html')
        