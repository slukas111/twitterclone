from django.contrib import admin
from twitteruser.models import CustomUser
from django.contrib.auth.admin import UserAdmin





admin.site.register(CustomUser, UserAdmin)