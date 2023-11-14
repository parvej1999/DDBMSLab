from django.urls import path, include
from . import views



urlpatterns = [
    path("", views.demoview, name = "form"),
    path("insert/", views.bulkDataEntry, name = "bulkdataentry"),
    path("delete/", views.bulkDataDelete, name = "bulkdatadelete"),
]