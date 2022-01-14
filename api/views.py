from api.serializers import RouteSerializer, LocationSerializer
from rest_framework import viewsets, permissions
from api.models import Route, Location


class RouteViewSet(viewsets.ModelViewSet):
  queryset = Route.objects.all()
  serializer_class = RouteSerializer
  #permission_classes = [permissions.IsAuthenticated]

class LocationViewSet(viewsets.ModelViewSet):
  queryset = Location.objects.all()
  serializer_class = LocationSerializer
  #permission_classes = [permissions.IsAuthenticated]
