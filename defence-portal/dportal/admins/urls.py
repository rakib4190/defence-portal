from django.contrib import admin
from django.urls import path
from .import views

app_name = 'admins'
urlpatterns = [
    path('dashboard/', views.dashboard, name='homepage'),
    path('all-student/', views.student, name='studentList'),
    path('addstudentform/', views.addStudent_page, name='addstudentform'),
    path('add-student/', views.addStudent, name='addstudent'),
    path('update-student/<int:id>/', views.updateStudent, name='updateStudent'),
    path('delete-student/<int:id>/', views.deleteStudent, name='deleteStudent'),
    path('all-teacher/', views.viewTeacher, name='teacherList'),
    path('add-teacher/', views.addTeacher, name='addteacher'),
    path('update-teacher/<int:id>/', views.updateTeacher, name='updateTeacher'),
    path('delete-teacher/<int:id>/', views.deleteTeacher, name='deleteTeacher'),
    path('non-assign-student-list/',
         views.nonAssignStudent, name='nonAssignStudent'),
    path('assign-supervisor/', views.assginSupervisor, name='assignSupervisor'),
    path('proposal/', views.proposal, name='proposalList'),
    path('update-defence-proposal/<int:pid>/',
         views.updateDefenceProposal, name='updateDefenceProposal'),
    path('details-proposalview/<int:pid>/',
         views.detailsDefenceProposal, name='detailsDefenceProposal'),
    path('delete-proposal/<int:id>/', views.deleteProposal, name='deleteProposal'),

    path('assigned-student/', views.assignedStudent, name='assignedStudent'),
    path('change_supervisor/<int:id>/',
         views.changeSupervisor, name='changeSupervisor'),
    path('supervisor-summary/', views.supervisorSummary, name='supervisorSummary'),

    path('view-semester/', views.viewSemester, name='viewSemester'),
    path('add-semester/', views.addSemester, name='addSemester'),
    path('update-semester/<int:id>/', views.updateSemester, name='updateSemester'),
    path('delete-semester/<int:id>/', views.deleteSemester, name='deleteSemester'),
    path('all-notice/', views.viewNotice, name='notice'),
    path('add-notice/', views.addNotice, name='addNotice'),
    path('update-notice/<int:id>/', views.updateNotice, name='updateNotice'),
    path('delete-notice/<int:id>/', views.deleteNotice, name='deleteNotice'),
    path('student-result/', views.results, name='result'),
    path('add-result/<int:id>/', views.addResult, name='addResult'),


    path('change-password/', views.changePassword, name='changePassword'),
    #path('profile/', views.admin_profile, name='profile'),

]
