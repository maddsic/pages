from django.urls import path

from .views import HomePageView, AboutPageView #importing our homepage templates from views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]

