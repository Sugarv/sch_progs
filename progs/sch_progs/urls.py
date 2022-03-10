from django.urls import path
from sch_progs.views import ProgramCreateView, ProgramListView, ProgramUpdateView
from . import views

urlpatterns = [
    path('', ProgramListView.as_view(), name='program_list'),
    path('add/', ProgramCreateView.as_view(), name='program_add'),
    path('edit/<int:pk>/', ProgramUpdateView.as_view(), name='program_edit'),

]