# models.py
from django.db import models
from users.models import User


class ModelStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=10)
    remaining_displays = models.IntegerField(default=20)
    displays_today = models.IntegerField(default=0)
    displays_this_week = models.IntegerField(default=0)
    displays_all_time = models.IntegerField(default=0)
    description = models.CharField(max_length=255, default='')
