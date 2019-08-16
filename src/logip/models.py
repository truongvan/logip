import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .tools import token_generator


class LogIPManager(models.Manager):
    def custom_create(self, ip, machine=""):
        log_ip = self.last()
        save_ip = ''
        if log_ip:
            save_ip = log_ip.ip
        if save_ip != ip:
            return self.create(ip=ip, machine=machine)
        return log_ip


class LogIP(models.Model):
    ip = models.GenericIPAddressField()
    machine = models.CharField(max_length=50, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = LogIPManager()


class AccessToken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        User, verbose_name=_("user"), on_delete=models.CASCADE)
    updated_at = models.DateTimeField(
        _("Updated at"), auto_now=True, auto_now_add=False)

    def gen_token(self):
        return token_generator.make_token(self)

    def check_token(self, token):
        return token_generator.check_token(self, token)
