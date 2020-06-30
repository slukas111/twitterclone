from django.db import models
from twitteruser.models import CustomUser
from tweet.models import Tweet


class Notification(models.Model):
    contact_user = models.ForeignKey(CustomUser, related_name="contact_user", on_delete=models.CASCADE)
    notification = models.BooleanField(default=False)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return self.tweet
