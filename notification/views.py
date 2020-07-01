from django.shortcuts import render, HttpResponseRedirect
from .models import Notification
from twitteruser.models import CustomUser 
# Create your views here.

def notification(request):
    html = "notifications.html"
    user = request.user
    notify = Notification.objects.filter(contact_user=user)
    for notification in notify:
        notification.delete()
    return render(request, html, { "notify": notify })