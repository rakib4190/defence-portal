from django.contrib import admin
from django.urls import path
from .import views

app_name = 'teacher'
urlpatterns = [


    path('t-dashboard/', views.dashboard, name='homepage'),
    path('supervised-student/', views.supervisedStudent, name='supervisedStudent'),
    path('send-message/<int:id>/', views.sendMessage, name='sendStudentMessage'),


]
