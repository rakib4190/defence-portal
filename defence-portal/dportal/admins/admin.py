from django.contrib import admin
from admins.models import AssignedStudent, Notice, Semester
# Register your models here.
admin.site.register(AssignedStudent)
admin.site.register(Notice)
admin.site.register(Semester)
