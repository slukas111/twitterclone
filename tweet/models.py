from django.db import models
from django.utils import timezone
from twitteruser.models import CustomUser

# Create your models here.
class Tweet(models.Model):
    tweet = models.CharField(max_length=140)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tweet