from core.mixins import ModelMixin
from django.db import models
from shapely import geometry  # noqa


class User(ModelMixin):
    class TypeUser(models.IntegerChoices):
        SPECIAL = 1, "special"
        NORMAL = 2, "normal"
        LABORIOUS = 3, "laborious"

    type = models.IntegerField(verbose_name="Type", choices=TypeUser.choices)
    gender = models.CharField(verbose_name="Gender", max_length=1)
    birthday = models.DateTimeField(verbose_name="Birthday")
    nationality = models.CharField(verbose_name="Nationality", max_length=2)
    email = models.EmailField(verbose_name="Email", unique=True)
    registered = models.DateTimeField(verbose_name="Birthday")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    @staticmethod
    def check_type(
        latitude: str,
        longitude: str,
    ) -> str:
        if latitude and longitude:
            point = geometry.Point(float(longitude), float(latitude))
            special = geometry.Polygon(
                [
                    (-2.196998, -46.361899),
                    (-15.411580, -34.276938),
                    (-19.766959, -52.997614),
                    (-23.966413, -44.428305),
                ]
            )
            normal = geometry.LineString(
                [(-26.155681, -54.777426), (-34.016466, -46.603598)]
            )
            if special.contains(point):
                return "special"
            elif normal.contains(point):
                return "normal"
            else:
                return "laborious"
