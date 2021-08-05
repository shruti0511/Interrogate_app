from quora.models import quoraTopic
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    employment = models.CharField(max_length=100, blank=True)
    school = models.CharField(max_length=100, blank=True)
    topics = models.ManyToManyField(quoraTopic)
    userImage = models.ImageField(upload_to = 'auth/userImg/', default = 'user.png')

    def __str__(self):
        return self.user.username
