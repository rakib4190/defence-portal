from django.contrib import admin
from django.urls import path
from .import views

app_name = 'login'
urlpatterns = [
    path('', views.welcome, name='homepage'),
    path('login-page/', views.login_page, name='login'),
    path('login/', views.user_login, name='userlogin'),
    path('student-registration/', views.studentRegistration, name='studentRegistration'),
    path('logout/', views.user_logout, name='logout'),


]
