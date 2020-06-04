from django.contrib import admin
from django.urls import path
from authentication import views

urlpatterns = [
    path("register/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
