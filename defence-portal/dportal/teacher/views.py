from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from admins.models import AssignedStudent
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from login.models import *


@login_required
def dashboard(request):
    return render(request, 'App-teacher/dashboard.html')


@login_required
def supervisedStudent(request):
    teacher_obj = Teacher.objects.get(admin=request.user.id)
    self_student_list = AssignedStudent.objects.filter(teacher_id=teacher_obj)
    diction = {'self_student_list': self_student_list}
    return render(request, 'App-teacher/supervised_student.html', context=diction)


@login_required
def sendMessage(request, id):
    message = AssignedStudent.objects.get(id=id)
    if request.method == "POST":
        message_title = request.POST.get("message_title")
        message_body = request.POST.get("message_body")
        message.message_title = message_title
        message.message_body = message_body
        message.save()
        return HttpResponseRedirect(reverse("teacher:supervisedStudent"))
    return render(request, 'App-teacher/message.html')
