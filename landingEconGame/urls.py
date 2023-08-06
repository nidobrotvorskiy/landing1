# lending_site/urls.py
from django.contrib import admin
from django.urls import path, include

from finance_game.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home)
    ]
