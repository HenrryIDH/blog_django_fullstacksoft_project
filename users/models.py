from django.db import models
from email.policy import default
from django.contrib.auth.models import User

def user_profile_path(instance, filename):
    return f"user/{instance.user.id}/{filename}"

# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_profile_path, default='avatar.png')
    bio = models.TextField(null=True, blank = True)

    def __str__(self):
        return self.user.username

        


