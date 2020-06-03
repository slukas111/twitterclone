from django.contrib import admin
from django.contrib.auth.admin import CustomUser
from twitteruser.models import CustomUserAdmin


admin.site.register(CustomUser, CustomUserAdmin)