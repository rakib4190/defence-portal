from ast import Delete
from unicodedata import name
from django.shortcuts import render
from .forms import *
from login.models import *
from admins.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

# Create your views here.


@login_required
def dashboard(request):
    admin = SuperAdmin.objects.all()
    admin_count = admin.count()
    teacher = Teacher.objects.all()
    teacher_count = teacher.count()
    student = Student.objects.all()
    student_count = student.count()
    total_proposal = DefenceProposal.objects.all()
    proposal_count = total_proposal.count()
    mid_term_done = AssignedStudent.objects.filter(mid_status=1)
    mid_term_done_count = mid_term_done.count()
    final_term_done = AssignedStudent.objects.filter(final_status=1)
    final_term_done_count = final_term_done.count()
    diction = {'admin_count': admin_count,
               'teacher_count': teacher_count,
               'student_count': student_count,
               'proposal_count': proposal_count,
               'mid_term_done_count': mid_term_done_count,
               'final_term_done_count': final_term_done_count}

    return render(request, 'App-admin/dashboard.html', context=diction)


@login_required
def student(request):
    student_list = Student.objects.all()
    diction = {'student_list': student_list}
    return render(request, 'App-admin/student.html', context=diction)


@login_required
def addStudent_page(request):
    return render(request, 'App-admin/addstudent.html')


@login_required
def addStudent(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(
                username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=3)
            user.student.address = address
            user.save()
            messages.success(request, "Successfully Added Student")
            return HttpResponseRedirect(reverse("admins:studentList"))
        except:
            messages.error(request, "Failed to Add Staff")
            return HttpResponseRedirect(reverse("admins:addstudent"))


@login_required
def updateStudent(request, id):
    student = Student.objects.get(admin=id)
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = CustomUser.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.password = password
        user.save()
        messages.success(request, "Successfully Updated Student")
        return HttpResponseRedirect(reverse("admins:studentList"))
    return render(request, 'App-admin/update_student.html', {'student': student})


@login_required
def deleteStudent(request, id):
    if request.method == "POST":
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect(reverse("admins:studentList"))


@login_required
def viewTeacher(request):
    teacher_list = Teacher.objects.all()
    diction = {'teacher_list': teacher_list}
    return render(request, 'App-admin/teacher.html', context=diction)


@login_required
def addTeacher(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        teacher_initial = request.POST.get("teacher_initial")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = CustomUser.objects.create_user(
            username=username, password=password, email=email, last_name=last_name, first_name=first_name, user_type=2)
        user.teacher.teacher_initial = teacher_initial
        user.teacher.phone_number = phone_number
        user.save()
        messages.success(request, "Successfully Added Teacher")
        return HttpResponseRedirect(reverse("admins:teacherList"))
    return render(request, 'App-admin/addteacher.html')


@login_required
def updateTeacher(request, id):
    teacher = Teacher.objects.get(admin=id)
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        teacher_initial = request.POST.get("teacher_initial")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = CustomUser.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.password = password
        user.save()
        teacher_model = Teacher.objects.get(admin=id)
        teacher_model.teacher_initial = teacher_initial
        teacher_model.phone_number = phone_number
        teacher_model.save()
        messages.success(request, "Successfully Added Teacher")
        return HttpResponseRedirect(reverse("admins:teacherList"))
    return render(request, 'App-admin/update_teacher.html', {'teacher': teacher})


@login_required
def deleteTeacher(request, id):
    if request.method == "POST":
        pi = Teacher.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect(reverse("admins:teacherList"))


@login_required
def nonAssignStudent(request):
    defence_proposal_list = DefenceProposal.objects.all()
    semester_list = Semester.objects.all()
    diction = {'defence_proposal_list': defence_proposal_list,
               'semester_list': semester_list}
    return render(request, 'App-admin/assign_supervisor.html', context=diction)


@login_required
def assginSupervisor(request):
    supervisor_list = Teacher.objects.all()
    student_list = Student.objects.all()
    diction = {'supervisor_list': supervisor_list,
               'student_list': student_list}
    if request.method == 'POST':
        student_id = request.POST.get("student_id")
        student = Student.objects.get(id=student_id)
        teacher_id = request.POST.get("teacher_id")
        teacher = Teacher.objects.get(id=teacher_id)
        assign = AssignedStudent(
            teacher_id=teacher, student_id=student, mid_status=0, final_status=0)
        assign.save()
        return HttpResponseRedirect(reverse("admins:nonAssignStudent"))

    return render(request, 'App-admin/assign_supervisor_form.html', context=diction)


@login_required
def changeSupervisor(request, id):
    supervisor_list = Teacher.objects.all()

    result = AssignedStudent.objects.get(id=id)
    print(result)
    if request.method == "POST":
        mid_status = request.POST.get("mid_status")
        result.teacher_id_id = mid_status
        result.save()
        return HttpResponseRedirect(reverse("admins:assignedStudent"))
    return render(request, 'App-admin/change_supervisor.html', {'supervisor_list': supervisor_list})


@login_required
def proposal(request):
    defence_proposal_list = DefenceProposal.objects.all()
    semester_list = Semester.objects.all()
    diction = {'defence_proposal_list': defence_proposal_list,
               'semester_list': semester_list}
    return render(request, 'App-admin/view_defence_proposal.html', context=diction)


@login_required
def updateDefenceProposal(request, pid):
    semester_list = Semester.objects.all()
    proposal = DefenceProposal.objects.get(id=pid)
    if request.method == "POST":
        credit_complete = request.POST.get("credit_complete")
        current_cgpa = request.POST.get("current_cgpa")
        semester = request.POST.get("semester")
        working_area = request.POST.get("working_area")
        defence_type = request.POST.get("defence_type")
        defence_title = request.POST.get("defence_title")
        defence_description = request.POST.get("defence_description")
        proposal.credit_complete = credit_complete
        proposal.current_cgpa = current_cgpa
        proposal.semester = semester
        proposal.working_area = working_area
        proposal.defence_type = defence_type
        proposal.defence_title = defence_title
        proposal.defence_description = defence_description
        proposal.save()
        return HttpResponseRedirect(reverse("admins:proposalList"))
    return render(request, 'App-admin/update_defence_proposal.html', {'semester_list': semester_list, 'proposal': proposal})


def detailsDefenceProposal(request, pid):
    proposal = DefenceProposal.objects.get(id=pid)
    return render(request, 'App-admin/details_defence_proposal.html', {'proposal': proposal})


@login_required
def deleteProposal(request, id):
    if request.method == "POST":
        pi = DefenceProposal.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect(reverse("admins:proposalList"))


@login_required
def assignedStudent(request):
    assigned_student_list = AssignedStudent.objects.all()
    semester_list = Semester.objects.all()
    diction = {'assigned_student_list': assigned_student_list,
               'semester_list': semester_list}
    return render(request, 'App-admin/assigned_student.html', context=diction)


@login_required
def supervisorSummary(request):
    return render(request, 'App-admin/supervisor_summary.html')


def viewNotice(request):
    notice_list = Notice.objects.all()
    diction = {'notice_list': notice_list}
    return render(request, 'App-admin/view_notice.html', context=diction)


@login_required
def addNotice(request):
    if request.method == "POST":
        form = AddNotice(request.POST)
        if form.is_valid():
            notice_title = form.cleaned_data['notice_title']
            notice_description = form.cleaned_data['notice_description']
            NewNotice = Notice(notice_title=notice_title,
                               notice_description=notice_description)
            NewNotice.save()
            return HttpResponseRedirect(reverse("admins:notice"))
    else:
        form = AddNotice()
    return render(request, 'App-admin/add_notice.html', {'form': form})


@login_required
def updateNotice(request, id):
    if request.method == 'POST':
        ni = Notice.objects.get(pk=id)
        form = AddNotice(request.POST, instance=ni)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admins:notice"))
    else:
        ni = Notice.objects.get(pk=id)
        form = AddNotice(instance=ni)
    return render(request, 'App-admin/update_notice.html', {'form': form})


@login_required
def deleteNotice(request, id):
    if request.method == "POST":
        pi = Notice.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect(reverse("admins:notice"))


@login_required
def viewSemester(request):
    semester_list = Semester.objects.all()
    diction = {'semester_list': semester_list}
    return render(request, 'App-admin/view_semester.html', context=diction)


@login_required
def addSemester(request):
    if request.method == "POST":
        form = AddSemester(request.POST)
        if form.is_valid():
            semester_name = form.cleaned_data['semester_name']
            NewSemester = Semester(semester_name=semester_name,)
            NewSemester.save()
            return HttpResponseRedirect(reverse("admins:viewSemester"))
    else:
        form = AddSemester()
    return render(request, 'App-admin/add_semester.html', {'form': form})


@login_required
def updateSemester(request, id):
    if request.method == 'POST':
        ni = Semester.objects.get(pk=id)
        form = AddSemester(request.POST, instance=ni)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admins:viewSemester"))
    else:
        ni = Semester.objects.get(pk=id)
        form = AddSemester(instance=ni)
    return render(request, 'App-admin/update_semester.html', {'form': form})


@login_required
def deleteSemester(request, id):
    if request.method == "POST":
        pi = Semester.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect(reverse("admins:viewSemester"))


@login_required
def results(request):
    assigned_student_list = AssignedStudent.objects.all()
    return render(request, 'App-admin/student_result.html', {'assigned_student_list': assigned_student_list})


@login_required
def addResult(request, id):
    result = AssignedStudent.objects.get(id=id)
    if request.method == "POST":
        mid_status = request.POST.get("mid_status")
        final_status = request.POST.get("final_status")
        result.mid_status = mid_status
        result.final_status = final_status
        result.save()
        return HttpResponseRedirect(reverse("admins:result"))
    return render(request, 'App-admin/add_result.html')


@login_required
def changePassword(request):
    return render(request, 'App-admin/change_password.html')


# def admin_profile(request):
    #user = CustomUser.objects.get(id=request.user.id)
    # return render(request, "App-admin/admin_profile.html", {"user": user})
