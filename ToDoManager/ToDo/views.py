from django.shortcuts import render, redirect, get_object_or_404
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
    tasks = Task.objects.filter(user_id=request.user, is_completed=False)
    return render (request, 'tasks.html', {'tasks': tasks})

@login_required(login_url='/login')
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
                priority=form.cleaned_data['priority'],
                user_id=request.user 
            )
        return redirect('tasks')

@login_required
def mark_completed(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        task.is_completed = True
        task.save()
    return redirect('tasks')

@login_required
def edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "GET":
        form = CreateTaskForm(initial={
            'title': task.title,
            'description': task.description,
            'priority': task.priority
        })
        return render(request, 'edit.html', {'task': task, 'form': form})
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.priority = form.cleaned_data['priority']
            task.save()
            return redirect('tasks')