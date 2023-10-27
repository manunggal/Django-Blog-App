from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView # --> import the class based views

urlpatterns = [
    # path's url argument is left empty if we want to set it as the homepage
    path("", PostListView.as_view(), name = "blog-home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name = "post-detail"), # pk stands for primary key
    path("post/new/", PostCreateView.as_view(), name = "post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name = "post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name = "post-delete"),  
    path("about/", views.about, name = "blog-about")
]