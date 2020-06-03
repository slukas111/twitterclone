"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic.base import TemplateView
# from authentication.urls import urlpatterns as auth_urls

# urlpatterns = [
#     path("", TemplateView.as_view(template_name="home.html"), name="home"),
#     path("admin/", admin.site.urls),

# ]
# urlpatterns += auth_urls

from django.contrib import admin
from django.urls import path
from authentication.urls import urlpatterns as auth_urls
from twitteruser.urls import urlpatterns as twitteruser_urls


urlpatterns = [
    path("admin/", admin.site.urls),
]
urlpatterns += auth_urls
urlpatterns += twitteruser_urls
