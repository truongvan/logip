import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from .models import LogIP

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class Index(View):

    def get(self, request):
        data = {}
        query = LogIP.objects.last()
        if query:
            data['ip'] = query.ip
            data['created_at'] = query.created_at
        return JsonResponse(data)


class UpdateIp(View):
    def get(self, request):
        new_ip = request.GET.get('ip')
        if not new_ip:
            new_ip = get_client_ip(request)
        if new_ip:
            data = {'ip': new_ip}
            try:
                LogIP.objects.create(ip=new_ip)
                data['ok'] = True
            except TypeError:
                data['ok'] = False
            return JsonResponse(data)