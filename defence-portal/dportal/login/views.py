import re
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from login.EmailBackEnd import EmailBackEnd
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from login.models import *
from django.contrib.auth.models import Group
from django.contrib import messages


def welcome(request):
    return render(request, 'App-login/welcome.html')


def studentRegistration(request):
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = CustomUser.objects.create_user(
            username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=3)
        user.save()
        messages.success(request, "Successfully Added Student")
        return HttpResponseRedirect(reverse("login:login"))

    return render(request, 'App-login/register.html')


def login_page(request):
    return render(request, 'App-login/login.html')


def user_login(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get(
            "email"), password=request.POST.get("password"))

        if user != None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse('admins:homepage'))
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse('teacher:homepage'))
            elif user.user_type == "3":
                return HttpResponseRedirect(reverse('student:homepage'))
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect(reverse('login:login'))


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login:login'))
