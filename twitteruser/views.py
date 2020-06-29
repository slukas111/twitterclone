from django.shortcuts import render
from twitteruser.models import CustomUser
from twitterclone.settings import AUTH_USER_MODEL
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet

@login_required
def index(request):
    html = "index.html"
    user_data = CustomUser.objects.all()
    tweet_data = Tweet.objects.all().order_by('-post_time')

    return render(request, html, {"user_data": user_data, "tweet_data": tweet_data, "auth_user": AUTH_USER_MODEL})

def author_detail(request, id):
    html ="author_page.html"
    author = CustomUser.objects.get(id=id)
    user_tweets = Tweet.objects.filter(author=author.id)
    return render(request, html, {'user_tweets': user_tweets, 'author': author})
