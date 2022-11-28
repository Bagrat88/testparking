from rest_framework import serializers

from parking.models import ParkingZone


class ParkingZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingZone
        fields = ["address"]
