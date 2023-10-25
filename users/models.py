from django.db import models
from django.contrib.auth.models import User # User model
from PIL import Image # Python Image Library

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # one to one relationship, if user is deleted, delete profile
    image = models.ImageField(default="default.jpg", upload_to="profile_pics") # default.jpg is the default image if no image is uploaded, upload_to is the directory where the image is uploaded

    def __str__(self): # dunder method, string representation of the model
        return f"{self.user.username} Profile"

    def save(self):
        super().save() # run the save method of the parent class

        img = Image.open(self.image.path) # open the image of the current instance
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300) # tuple, resize the image to 300x300
            img.thumbnail(output_size)
            img.save(self.image.path)       
       
# Create your models here.
