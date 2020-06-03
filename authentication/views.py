from django.shortcuts import render, HttpResponseRedirect
# from customuser.settings import AUTH_USER_MODEL
from twitteruser.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from .forms import *
from twitteruser.forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def signup_view(request):
    html = "register.html"

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newuser = CustomUser.objects.create(
                username=data["username"],
                password=data["password"],
                display_name=data["display_name"],
            )
            newuser.set_password(raw_password=data["password"])
            newuser.save()
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            login(request, user)

        return HttpResponseRedirect(reverse("home"))
    else:
        form = SignUpForm()
    return render(request, html, {"form": form})


def login_view(request):
    html = "login.html"

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)

            return HttpResponseRedirect(request.GET.get("next", reverse("home")))
    else:
        form = LoginForm()
    return render(request, html, {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))