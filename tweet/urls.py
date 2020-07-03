from django.contrib import admin
from django.urls import path
from . import views
from tweet.views import *

urlpatterns = [
    path('',Tweets.as_view(), name="home"),
    path('generic_tweet/', add_tweet, name='add_tweet'),
    path('tweet/<int:id>/', tweet_view, name='tweet_view'),

]