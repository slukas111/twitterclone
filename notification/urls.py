from django.contrib import admin
from django.urls import path
# from authentication.views import * 
from .views import *


urlpatterns = [

    path('notification/', notification, name="notification"),

]