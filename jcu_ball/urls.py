"""JCU Ball URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from . import views

app_name = 'jcu_ball'
urlpatterns = [
    path("", views.BallReservationListView.as_view(), name="reservation_home"),
    path("reservations/", views.BallReservationListView.as_view(), name="reservation_list"),
    path(
        "reservations/add", views.BallReservationAddView.as_view(), name="reservation_add"
    ),
    path(
        "reservations/<int:pk>/edit",
        views.BallReservationEditView.as_view(),
        name="reservation_edit",
    ),
    path(
        "reservations/<int:pk>/delete",
        views.BallReservationDeleteView.as_view(),
        name="reservation_delete",
    ),
    path("reservations/export/", views.export_csv, name="reservation_export"),
]
