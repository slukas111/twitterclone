# from django.db import models
# from twitteruser.models import TwitterUser
# from django.utils import timezone

# # Create your models here.
# class Tweet(models.Model):
#     tweet = models.CharField(max_length=140)
#     author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
#     date = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.tweet
