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


urlpatterns = [
    path("", index,  name="home"),
    path("signup/", sign_up, name="signup"),
    path("login/", log_in, name="login"),
    path("logout/", log_out, name="logout"),
]