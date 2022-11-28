from rest_framework import generics

from .models import ParkingZone
from .serializers import ParkingZoneSerializer


class Parking(generics.ListAPIView):
    serializer_class = ParkingZoneSerializer
    queryset = ParkingZone.objects.all()

