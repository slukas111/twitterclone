from django.shortcuts import render, HttpResponseRedirect
from twitterclone.settings import AUTH_USER_MODEL
from twitteruser.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import View

class SignUp(View):
    def get(self,request):
        html = "signup.html"
        form = SignUpForm()
        return render(request, html, {'form': form})

    def post(self, request):
        html = "signup.html"
        form = SignUpForm(request.POST)
        # if request.method == "POST":
        #     form = SignUpForm(request.POST)
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
        # else:
        form = SignUpForm()
        return render(request, html, {"form": form})


def log_in(request):
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


def log_out(request):
    logout(request)
    return (HttpResponseRedirect("/login/"))