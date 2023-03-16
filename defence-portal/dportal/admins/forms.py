from cProfile import label
from dataclasses import field
from tkinter import Widget
from django import forms
from admins.models import *
from login.models import *


class AddNotice(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['notice_title', 'notice_description']
        labels = {'notice_title': 'Enter Title',
                  'notice_description': 'Notice Description'}

        widgets = {
            'notice_title': forms.TextInput(attrs={'class': 'form-control'}),
            'notice_description': forms.TextInput(attrs={'class': 'form-control'}),

        }


class AddSemester(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['semester_name']
        labels = {'semester_name': 'Enter Semester Name'}

        widgets = {
            'semester_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
