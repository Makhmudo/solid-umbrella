from .views import HomePageView, AboutPageView
from django.urls import path

urlpatterns = [
    # path('', homePageView, name='home'),
    path('', HomePageView.as_view(), name='homepage'),
    path('about/', AboutPageView.as_view(), name='about')
]