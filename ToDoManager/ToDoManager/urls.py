from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from ToDo.views import index_page, register_page, tasks_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index'),
    path('register/', register_page, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('tasks/', tasks_page, name='tasks')
]
