from django.urls import path
from .views import AboutPageView, HomePageView, WeddingPageView, ScratchPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("wedding/", WeddingPageView.as_view(), name="wedding"),
    path("scratch/", ScratchPageView.as_view(), name="scratch"),
]
