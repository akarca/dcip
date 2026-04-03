from django.urls import path

from . import views

urlpatterns = [
    path("api/dcip/<str:ip>/", views.check_api, name="dcip-api"),
    path("datacenter-ip-checker/", views.check_page, name="dcip-check"),
]
