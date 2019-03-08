from django.urls import path
from .views import Index, UpdateIp

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('update/', UpdateIp.as_view(), name='update')
]
