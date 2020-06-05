from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Tweet
from twitteruser.models import CustomUser
from .forms import TweetForm

#Got help from chris on tweet

def tweets(request):
    html = "tweet.html"
    tweets = Tweet.objects.all().order_by('-post_time')

    return render(request, html, {"tweets": tweets})

def add_tweet(request):
    form = TweetForm()
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            Tweet.objects.create(
                tweet = data['tweet'],
                author = request.user
            )
        # form.save()
        return HttpResponseRedirect(reverse("home"))
    return render(request, 'generic_tweet.html',{'form':form})

def tweet_view(request, id):
    data = Tweet.objects.get(id=id)
    return render(request, 'tweet.html', {'data': data})