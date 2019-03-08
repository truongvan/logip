from django.db import models


class LogIP(models.Model):
    ip = models.GenericIPAddressField()
