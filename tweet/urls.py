from django.contrib import admin
from django.urls import path
from . import views
from tweet.views import *

urlpatterns = [
    path('tweet/', tweets, name="tweet"),
    path('tweetadd/', add_tweet, name='tweetadd'),
    path('tweet/<int:id>', tweet_view, name='tweetview'),

]