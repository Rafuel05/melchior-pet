from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html',
        next_page='home'
    ), name='login'),
    path('logout/', views.custom_logout, name='logout'),
]
