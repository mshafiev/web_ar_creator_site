from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        unique=True,
    )

    email_verify = models.BooleanField(default=False)

    free_models_count = models.IntegerField(default=2)
