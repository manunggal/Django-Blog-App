from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE) # --> 1. author using user table, 2. on_delete: if the user is deleted, the post will be deleted as well

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # --> return the url as a string, 
        # reverse will return the full path as a string, 
        # kwargs is a dictionary that maps the url pattern to the value of the primary key of the post
        return reverse('post-detail', kwargs = {'pk': self.pk}) 


# Path: django_project/blog/views.py
# Compare this snippet from django_project/blog/urls.py: