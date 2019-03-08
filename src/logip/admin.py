from django.contrib import admin

from .models import LogIP


class LogipAdmin(admin.ModelAdmin):
    pass


admin.site.register(LogIP, LogipAdmin)
