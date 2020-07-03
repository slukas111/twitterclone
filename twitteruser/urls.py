# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns=[
#     path("", views.index, name="home"),
#     path("register/", views.signup_view, name="signup"),
#     path("login/", views.login_view, name="login"),
#     path("logout/", views.logout_view, name="logout"),
# ]

from django.contrib import admin
from django.urls import path
from authentication.views import * 
from twitteruser.views import *
from . import views


urlpatterns = [

    path('author_detail/<int:id>/', author_detail, name="author_detail"),
    path('follow/<int:id>/', Follow.as_view(), name="follow"),
    path('unfollow/<int:id>/', Unfollow.as_view(), name="unfollow")
]