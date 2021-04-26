from django.db import models
from accounts.models.user import User
from core.mixins import ModelMixin


class Picture(ModelMixin):

    large = models.CharField(verbose_name="Large", max_length=100)
    medium = models.CharField(verbose_name="Medium", max_length=100)
    thumbnail = models.CharField(verbose_name="Thumbnail", max_length=100)
    user = models.ForeignKey(User, related_name="pictures", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Picture"
        verbose_name_plural = "Pictures"
