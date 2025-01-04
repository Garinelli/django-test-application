from django.contrib import admin
from django.urls import path
from ToDo.views import index_page, register_page, login_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='index'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login')
]
