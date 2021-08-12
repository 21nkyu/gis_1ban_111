from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    success_url = reverse_lazy('articleapp:list')#디테일뷰가 없으니 임시로
    template_name = 'projectapp/create.html' #에서 시각화 할거다


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'