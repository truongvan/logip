import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from .models import LogIP


class Index(View):

    def get(self, request):
        data = {'ip': None}
        ip_in_params = request.GET.get('ip', '')
        if ip_in_params:
            try:
                LogIP.objects.create(ip=ip_in_params)
                return JsonResponse({'ok': True})
            except TypeError:
                return JsonResponse({'ok': False})
        else:
            try:
                query = LogIP.objects.last()
                data['ip'] = query.ip
            except LogIP.DoesNotExist:
                return JsonResponse(data)
            return JsonResponse(data)
