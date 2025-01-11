from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from ToDo.views import (
    index_page, register_page, tasks_page, create, mark_completed,
    edit, delete
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index'),
    path('register/', register_page, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('tasks/', tasks_page, name='tasks'),
    path('create/', create, name='create'),
    path('mark_completed/<int:task_id>/', mark_completed, name='mark_completed'),
    path('edit/<int:task_id>/', edit, name='edit'),
    path('delete/<int:task_id>', delete, name='delete')
]
