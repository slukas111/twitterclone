from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=50)
    following = models.ManyToManyField("self", related_name='follows', symmetrical=False)

    def __str__(self):
        return self.username
#mw or Janell Huyck
