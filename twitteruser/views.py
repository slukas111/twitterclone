from django.shortcuts import render, HttpResponseRedirect
from twitteruser.models import CustomUser
from twitterclone.settings import AUTH_USER_MODEL
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet

@login_required
def author_detail(request, id):
    html ="author_page.html"
    author = CustomUser.objects.get(id=id)
    user_tweets = Tweet.objects.filter(author=author.id).order_by('-post_time')
    all_followers = request.user.following.all()
    following_count = all_followers.count()
    tweet_count = user_tweets.count()
    return render(request, html, {
    'user_tweets': user_tweets, 
    'author': author,
    "all_followers": all_followers, 
    "following_count": following_count,
    "tweet_count": tweet_count,
    })

@login_required
def follow(request, id):
    html= "author_page.html"
    own_profile = request.user # or your queryset to get
    following_profile = CustomUser.objects.get(id=id)
    own_profile.following.add(following_profile)  # and .remove() for unfollow
    own_profile.save()
    # return render(request, html)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))

@login_required
def unfollow(request, id):
    html = "author_page.html"
    own_profile = request.user  # or your queryset to get
    following_profile = CustomUser.objects.get(id=id)
    own_profile.following.remove(following_profile)  # and .remove() for unfollow
    own_profile.save()
    # return render(request, html)
    #not pulling the correct id
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
