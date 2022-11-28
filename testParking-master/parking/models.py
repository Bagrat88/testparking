from django.db import models


class ParkingZone(models.Model):
    class Meta:
        app_label = "parking"
    address = models.CharField(max_length=255)
