
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
) # --> this mixin will require the user to be logged in to access the page

from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.shortcuts import render
from .models import Post # . before models indicates that models is in the same directory as views.py
# from django.http import HttpResponse --> removed, since we're using render now



def home(request):

    context = {
        'posts': Post.objects.all() # --> Post.objects.all() is a query set, which is a list of objects
        
    }

    # return HttpResponse('<h1>Blog Home</h1>') --> This is the old way of doing it
    return render(request, 'blog/home.html', context) # --> render still return an HttpResponse object, but it's a shortcut to make it easier to write the views


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html --> default template name
    context_object_name = 'posts' # default context_object_name is object_list
    ordering = ['-date_posted'] # - sign indicates that the newest post is on top

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content'] # fields that we want to be displayed in the form

    def form_valid(self, form):
        form.instance.author = self.request.user # set the author of the post to the current logged in user
        return super().form_valid(form) # run the form_valid method on the parent class

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content'] # fields that we want to be displayed in the form

    def form_valid(self, form):
        form.instance.author = self.request.user # set the author of the post to the current logged in user
        return super().form_valid(form) # run the form_valid method on the parent class

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # redirect to homepage after deleting a post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'Anjing'})


