from django.contrib import admin
from django.urls import path
from .import views

app_name = 'student'
urlpatterns = [


    path('s-dashboard/', views.dashboard, name='homepage'),
    path('proposal/', views.viewProposal, name='viewProposal'),
    path('submit-proposal-form/', views.submitProposalform,
         name='submitProposalform'),
    path('submitproposal/', views.submitProposal, name='submitProposal'),
    path('documents/', views.submitDocuments, name='submitDocuments'),
    path('middocuments/<int:id>/', views.submitMidDocuments, name='submitMidDocuments'),
    path('finaldocuments/<int:id>/', views.submitFinalDocuments, name='submitFinalDocuments'),
    path('supervisor/', views.supervisorDetails, name='supervisorDetails'),
    path('teacher-message/', views.teacherMessages, name='teacherMessage'),


]
