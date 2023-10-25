from django.shortcuts import render
from .models import Post # . before models indicates that models is in the same directory as views.py
# from django.http import HttpResponse --> removed, since we're using render now

# Dummy posts data to be deleted, since it is replace with real data from database
# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2021'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'August 28, 2021'
#     }
# ]

def home(request):

    context = {
        'posts': Post.objects.all() # --> Post.objects.all() is a query set, which is a list of objects
        
    }

    # return HttpResponse('<h1>Blog Home</h1>') --> This is the old way of doing it
    return render(request, 'blog/home.html', context) # --> render still return an HttpResponse object, but it's a shortcut to make it easier to write the views


def about(request):
    return render(request, 'blog/about.html', {'title': 'Anjing'})


