from django.contrib.auth.views import LogoutView
from django.urls import path, register_converter
from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/<int:pk>/', views.ProfileUser.as_view(), name='profile'),
]
