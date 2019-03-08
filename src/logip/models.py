from django.db import models


class LogIP(models.Model):
    ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
