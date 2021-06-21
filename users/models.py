from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/')
    location = models.CharField(default='Unknown', max_length=200)

    def __str__(self):
        return str(self.username)
