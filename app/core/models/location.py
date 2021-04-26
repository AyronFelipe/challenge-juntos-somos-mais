from core.mixins import ModelMixin
from django.db import models
from accounts.models.user import User


class Coordinates(models.Model):

    longitude = models.FloatField(verbose_name="Longitude")
    latitude = models.FloatField(verbose_name="Latitude")

    class Meta:

        verbose_name = "Coordinates"
        verbose_name_plural = "Coordinates"


class TimeZone(models.Model):

    offset = models.CharField(verbose_name="Offset", max_length=10)
    description = models.TextField(verbose_name="Description")

    class Meta:

        verbose_name = "Time Zone"
        verbose_name_plural = "Time Zones"


class Location(ModelMixin):

    street = models.CharField(verbose_name="Street", max_length=50)
    city = models.CharField(verbose_name="City", max_length=30)
    state = models.CharField(verbose_name="State", max_length=30)
    postcode = models.IntegerField(verbose_name="Post Code")
    coordinates = models.OneToOneField(
        Coordinates,
        related_name="location_coordinates",
        on_delete=models.SET_NULL,
        null=True,
    )
    timezone = models.OneToOneField(
        TimeZone, related_name="location_timezone", on_delete=models.SET_NULL, null=True
    )
    user = models.OneToOneField(
        User, related_name="location_user", on_delete=models.CASCADE
    )

    class Meta:

        verbose_name = "Location"
        verbose_name_plural = "Locations"
