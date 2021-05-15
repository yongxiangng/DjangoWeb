from django.urls import path
from .views import HomePageView, AboutPageView, AwardsPageView, ProjectsPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('awards/', AwardsPageView.as_view(), name='awards'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('', HomePageView.as_view(), name='home'),
]
