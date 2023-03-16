from django.db import models
from login.models import *

# Create your models here.


class DefenceProposal(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.CharField(max_length=70)
    credit_complete = models.IntegerField()
    current_cgpa = models.FloatField()
    working_area = models.CharField(max_length=200)
    defence_type = models.CharField(max_length=70)
    defence_title = models.CharField(max_length=100)
    defence_description = models.TextField()
    defence_status = models.IntegerField(default=0)
    assigned_status = models.IntegerField(default=0)
    objects = models.Manager()


class Documents(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    mid_document = models.CharField(max_length=500)
    mid_video = models.CharField(max_length=500)
    final_document = models.CharField(max_length=500)
    final_video = models.CharField(max_length=500)
    github_link = models.CharField(max_length=500)
    objects = models.Manager()
