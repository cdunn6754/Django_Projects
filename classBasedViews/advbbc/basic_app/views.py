from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)
from django.core.urlresolvers import reverse_lazy

from basic_app.models import School, Student
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    model = School
    context_object_name = 'schools'

class SchoolDetailView(DetailView):
    model = School
    template_name = 'basic_app/school_detail.html'
    context_object_name = 'school_detail'

class SchoolCreateView(CreateView):
    model = School
    fields = ('name', 'principal', 'location')

class SchoolUpdateView(UpdateView):
    model = School
    fields = ('name', 'principal')

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("basic_app:list")
