from django.urls import path

from . import views

app_name = 'summer_picnic'

urlpatterns = [
    path('reservations/', views.PicnicReservationListView.as_view(), name='reservation_list'),
    path('reservations/add/', views.PicnicReservationAddView.as_view(), name='reservation_add'),
    path('reservations/<int:pk>/edit/', views.PicnicReservationEditView.as_view(), name='reservation_edit'),
    path('reservations/<int:pk>/delete/', views.PicnicReservationDeleteView.as_view(), name='reservation_delete'),
    path('reservations/export/', views.export_csv, name='reservation_export'),
]