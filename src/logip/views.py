import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from .models import LogIP


class Index(View):

    def get(self, request):
        data = {}
        try:
            query = LogIP.objects.last()
            data['ip'] = query.ip
            data['created_at'] = query.created_at
        except LogIP.DoesNotExist:
            pass
        return JsonResponse(data)


class UpdateIp(View):
    def get(self, request):
        new_ip = request.META['REMOTE_ADDR']
        if new_ip:
            data = {'ip': new_ip}
            try:
                LogIP.objects.create(ip=new_ip)
                data['ok'] = True
            except TypeError:
                data['ok'] = False
            return JsonResponse(data)