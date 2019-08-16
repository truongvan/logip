import json
import datetime
import pytz

from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from .models import LogIP
from .token import check_access_id, check_token
from .tools import get_client_ip


class Index(View):
    def get(self, request):
        access_id = request.GET.get('access_id')
        if check_access_id(access_id):
            data = {}
            today_utc = datetime.datetime.today().replace(tzinfo=pytz.timezone('UTC'))
            query = LogIP.objects.filter(created_at__gte=today_utc)
            if query:
                data['ip'] = query.ip
                data['created_at'] = query.created_at
            return JsonResponse(data)
        return HttpResponseForbidden()


class UpdateIp(View):
    def get(self, request):
        new_ip = request.GET.get('ip')
        access_id = request.GET.get('access_id')
        token = request.GET.get('access_token')
        machine = request.GET.get('machine', "")
        if check_token(access_id, token):
            if not new_ip:
                new_ip = get_client_ip(request)
            if new_ip:
                data = {'ip': new_ip, 'machine': machine}
                try:
                    LogIP.objects.custom_create(ip=new_ip, machine=machine)
                    data['ok'] = True
                except TypeError:
                    data['ok'] = False
            return JsonResponse(data)
        return HttpResponseForbidden()
