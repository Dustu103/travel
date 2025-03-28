from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    profile_pic = models.CharField(
        max_length=250,
        default="https://drive.google.com/uc?id=1USSc1D8fjYqOHt7VbQmv3CK1njV2jGHR"
    )

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions",
        blank=True
    )
