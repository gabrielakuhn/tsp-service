from django.db import models

class Route(models.Model):
    """A class defining  the route."""
    # code = models.CharField(max_length=8, default="", unique=True)
    num_vehicles = models.IntegerField(null=False, default=1)
    depot = models.IntegerField(null=False, default=1)

class Location(models.Model):
    """A class defining  the locations."""
    name = models.CharField(max_length=50, unique=True)
    lat = models.DecimalField(max_digits=18, decimal_places=15, default=None, null=True, blank=True)     #https://docs.python.org/3/library/decimal.html#module-decimal
    lon = models.DecimalField(max_digits=18, decimal_places=15, default=None, null=True, blank=True)