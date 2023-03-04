import uuid
from django.db import models

class TimeStampUUIDModel(models.Model):
    pkid            = models.BigAutoField(primary_key=True, editable=False)
    id              = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at      = models.DateTimeField(auto_now_add=True) #auto_now_add will be added once and cannot be modified
    updated_at      = models.DateTimeField(auto_now=True) #auto_now can be modified

    class Meta:
        abstract = True
