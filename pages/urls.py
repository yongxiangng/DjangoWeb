from django.urls import path
from .views import HomePageView, AboutPageView, AwardsPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('awards/', AwardsPageView.as_view(), name='awards'),
    path('', HomePageView.as_view(), name='home'),
]
