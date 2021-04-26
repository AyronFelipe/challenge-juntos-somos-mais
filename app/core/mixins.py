import uuid

from django.db import models


class CreateAndUpdateMixin(models.Model):

    created_at = models.DateTimeField("Created at", auto_now_add=True, editable=False)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    class Meta:

        abstract = True


class ModelMixin(CreateAndUpdateMixin):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:

        abstract = True
