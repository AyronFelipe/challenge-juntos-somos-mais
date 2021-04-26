from django.db import models
from accounts.models.user import User
from core.mixins import ModelMixin


class Phone(ModelMixin):
    class TypePhone(models.IntegerChoices):
        CELL = 1, "cell"
        LAND = 2, "land"

    type = models.IntegerField(verbose_name="Type", choices=TypePhone.choices)
    number = models.CharField(verbose_name="Phone number", max_length=14)
    user = models.ForeignKey(User, related_name="phones", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"

    @staticmethod
    def transform(number: str) -> str:

        return number.replace("(", "+55").replace(") ", "").replace("-", "")
