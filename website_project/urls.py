"""website_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from projects import views as projects_view
from about import views as about_view
from awards import views as awards_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),    
    path('api/about/', about_view.get_about),
    path('api/about/', about_view.add_about),
    path('api/awards/', awards_view.add_award),
    path('api/awards/', awards_view.get_all_awards),
    path('api/awards/<str:award_title>', awards_view.get_award),
    path('api/projects/', projects_view.add_project),
    path('api/projects/', projects_view.get_all_projects),
    path('api/projects/<str:project_title>', projects_view.get_project),
]
