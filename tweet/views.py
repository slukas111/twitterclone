from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Tweet
from twitteruser.models import CustomUser
from .forms import TweetForm

#Got help from chris on tweet