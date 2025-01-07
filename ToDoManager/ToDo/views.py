from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, CreateTaskForm
from .models import User, Task

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
            return redirect('login')


@login_required(login_url='/login')
def tasks_page(request):
    return render (request, 'tasks.html')

@login_required
def create(request):
    if request.method == "GET":
        form = CreateTaskForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                user_id=request.user 
            )
        return redirect('tasks')