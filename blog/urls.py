from django.urls import path
from . import views

urlpatterns = [
    # path's url argument is left empty if we want to set it as the homepage
    path("", views.home, name = "blog-home"),
    path("about/", views.about, name = "blog-about")
]