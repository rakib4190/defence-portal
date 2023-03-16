from pyexpat import model
from django.db import models
from student.models import *
from teacher.models import *
from login.models import *

# Create your models here.


class AssignedStudent(models.Model):
    id = models.AutoField(primary_key=True)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_id = models.OneToOneField(
        Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    mid_status = models.IntegerField(default=0)
    final_status = models.IntegerField(default=0)
    message_title = models.CharField(max_length=250, default=0)
    message_body = models.TextField(max_length=500, default=0)
    mid_document = models.CharField(max_length=500, default=0)
    mid_video = models.CharField(max_length=500, default=0)
    final_document = models.CharField(max_length=500, default=0)
    final_video = models.CharField(max_length=500, default=0)
    github_link = models.CharField(max_length=500, default=0)
    objects = models.Manager()


class Semester(models.Model):
    id = models.AutoField(primary_key=True)
    semester_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    notice_title = models.CharField(max_length=200)
    notice_description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class StudentMark(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE)
