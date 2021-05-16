from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from posts.models import Post
from awards.models import Award
from projects.models import Project

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class AwardsPageView(ListView):
    model = Award
    template_name = 'award.html'
    context_object_name = 'all_awards_list'

class ProjectsPageView(ListView):
    model = Project
    template_name = 'project.html'
    context_object_name = 'all_projects_list'
    
class ProjectsPageDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
