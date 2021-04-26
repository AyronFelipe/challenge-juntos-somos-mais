from django.db import models
from core.mixins import ModelMixin
from .user import User


class Name(ModelMixin):

    title = models.CharField(verbose_name="Title", max_length=10)
    first = models.CharField(verbose_name="First Name", max_length=50)
    last = models.CharField(verbose_name="Last Name", max_length=50)
    user = models.OneToOneField(
        User, related_name="name_user", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Name"
        verbose_name_plural = "Names"

    def __str__(self):

        return f"{self.title} {self.first} {self.last}"
