from django.shortcuts import render

# Create your views here.
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from admins.models import *
from student.models import *

# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'App-student/dashboard.html')


@login_required
def submitDocuments(request):
    student_obj = Student.objects.get(admin=request.user.id)
    self_document = AssignedStudent.objects.filter(student_id=student_obj)
    return render(request, 'App-student/submit_documents.html', {'self_document': self_document})


@login_required
def submitMidDocuments(request, id):
    middoc = AssignedStudent.objects.get(id=id)
    if request.method == "POST":
        mid_doc_link = request.POST.get("mid_doc_link")
        mid_video_link = request.POST.get("mid_video_link")
        middoc.mid_document = mid_doc_link
        middoc.mid_video = mid_video_link
        middoc.save()
        return HttpResponseRedirect(reverse("student:submitDocuments"))
    return render(request, 'App-student/submit_mid_term.html')

@login_required
def submitFinalDocuments(request, id):
    finaldoc = AssignedStudent.objects.get(id=id)
    if request.method == "POST":
        final_doc_link = request.POST.get("final_doc_link")
        final_video_link = request.POST.get("final_video_link")
        code_link = request.POST.get("code_link")
        finaldoc.final_document = final_doc_link
        finaldoc.final_video = final_video_link
        finaldoc.github_link = code_link
        finaldoc.save()
        return HttpResponseRedirect(reverse("student:submitDocuments"))
    return render(request, 'App-student/submit_final_term.html')


@login_required
def viewProposal(request):
    student_obj = Student.objects.get(admin=request.user.id)
    self_proposal = DefenceProposal.objects.filter(student_id=student_obj)
    diction = {'self_proposal': self_proposal}
    return render(request, 'App-student/view_proposal.html', context=diction)


@login_required
def submitProposalform(request):
    semester_list = Semester.objects.all()
    diction = {'semester_list': semester_list}
    return render(request, 'App-student/submit_proposal.html', context=diction)


@login_required
def submitProposal(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        credit_complete = request.POST.get("credit_complete")
        current_cgpa = request.POST.get("current_cgpa")
        semester = request.POST.get("semester")
        working_area = request.POST.get("working_area")
        defence_type = request.POST.get("defence_type")
        defence_title = request.POST.get("defence_title")
        defence_description = request.POST.get("defence_description")
        student_obj = Student.objects.get(admin=request.user.id)
        try:
            proposal = DefenceProposal(student_id=student_obj, semester=semester, credit_complete=credit_complete, current_cgpa=current_cgpa, working_area=working_area,
                                       defence_type=defence_type, defence_title=defence_title, defence_description=defence_description, defence_status=0, assigned_status=0)
            proposal.save()
            messages.success(request, " Proposal Submitted Successfully")
            return HttpResponseRedirect(reverse("student:viewProposal"))

        except:
            messages.error(request, "Failed to Add Staff")
            return HttpResponseRedirect(reverse("student:submitProposalform"))


@login_required
def supervisorDetails(request):
    student_obj = Student.objects.get(admin=request.user.id)
    supervisor_details = AssignedStudent.objects.filter(student_id=student_obj)
    return render(request, 'App-student/supervisor_details.html', {'supervisor_details': supervisor_details})


@login_required
def teacherMessages(request):
    student_obj = Student.objects.get(admin=request.user.id)
    teacher_message = AssignedStudent.objects.filter(student_id=student_obj)
    return render(request, 'App-student/teacher_message.html', {'teacher_message': teacher_message})
