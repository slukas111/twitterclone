from django.contrib import admin
from django.urls import path
from authentication import views


urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("login/", views.log_in, name="login"),
    path("logout/", views.log_out, name="logout"),
]
