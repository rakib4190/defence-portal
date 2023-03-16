from django.db import models
from login.models import *
from admins.models import *
# Create your models here.


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    message_title = models.CharField(max_length=200)
    message_description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
