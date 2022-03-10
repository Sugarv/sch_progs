from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.http import HttpResponse

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Program
from .forms import ProgramForm

class ProgramListView(ListView):
    model = Program
    context_object_name = 'programs'
    
    # get school's programs
    def get_queryset(self, **kwargs):
        code = '1234567'
        qs = super().get_queryset()
        return qs.filter(school1__code=code)

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'sch_progs/program_form.html'

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'sch_progs/program_update_form.html'
    success_url = reverse_lazy('program_list')


def index(request):
    pass
