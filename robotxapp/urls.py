from django.urls import path
from .views import HomePageView, AboutView, ResearchView, VisionView, ContactView, NewsView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('/research/', ResearchView.as_view(), name='research'),
    path('/vision/', VisionView.as_view(), name='vision'),
    path('/contact/', ContactView.as_view(), name='contact'),
    path('/about/', AboutView.as_view(), name='about'),
    path('/news/', NewsView.as_view(), name='news'),
]