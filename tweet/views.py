from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Tweet
from twitteruser.models import CustomUser
from .forms import TweetForm
import re
from notification.models import Notification
from django.contrib.auth.decorators import login_required
# Got help from chris on tweet

@login_required
def tweets(request):
    html = "index.html"
    ur_tweets = Tweet.objects.filter(author=request.user).order_by("-post_time")
    following_tweets = Tweet.objects.filter(author__in=request.user.following.all())
    #https://www.dev2qa.com/what-does-double-underscore-__-means-in-django-model-queryset-objects-filter-method/
    tweets = ur_tweets | following_tweets #query set

    return render(request, html, {"tweets": tweets})

@login_required
def add_tweet(request):
    form = TweetForm()
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_tweet = Tweet.objects.create(tweet=data["tweet"], author=request.user)
            asign_user = re.findall(r"@\w+", data["tweet"])
            for mentioned in asign_user:
                Notification.objects.create(
                    tweet = new_tweet,
                    contact_user = CustomUser.objects.get(username=mentioned[1:])
                )

                
        return HttpResponseRedirect(reverse("home"))
    return render(request, "generic_tweet.html", {"form": form})


def tweet_view(request, id):
    data = Tweet.objects.get(id=id)
    return render(request, "tweet.html", {"data": data})

