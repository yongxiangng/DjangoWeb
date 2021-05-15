from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from posts.models import Post

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

class AboutPageView(TemplateView):
    template_name = 'about.html'
