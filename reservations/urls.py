"""reservations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from . import views

urlpatterns = [
    path('testing/', views.Testing.as_view(), name='testing'),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('reservations/', views.home, name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('jcu_ball/', include('jcu_ball.urls', namespace='jcu_ball')),
    path('summer_picnic/', include('summer_picnic.urls', namespace='summer_picnic')),
]


