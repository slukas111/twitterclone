from django.shortcuts import render
from twitteruser.models import CustomUser
from twitterclone.settings import AUTH_USER_MODEL
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    html = "index.html"
    data = CustomUser.objects.all()

    return render(request, html, {"data": data, "auth_user": AUTH_USER_MODEL})
