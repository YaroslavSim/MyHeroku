""""Models."""
from django.db import models


class Log(models.Model):
    """LoggerMiddleware class."""

    path = models.CharField(max_length=100)
    method = models.CharField(max_length=10)
    execution_time_sec = models.FloatField()