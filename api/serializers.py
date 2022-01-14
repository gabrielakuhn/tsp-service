from rest_framework import serializers
from api.models import Route, Location


class RouteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Route
    fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Location
    fields = '__all__'