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
from authentication import views 

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]