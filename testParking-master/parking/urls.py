from django.urls import path

from .views import Parking

app_name = "parking"

urlpatterns = [path("", Parking.as_view(), name="parking")]
