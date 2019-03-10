
from django.core.validators import ValidationError

from .models import AccessToken


def check_token(access_id, input_token):
    try:
        access_token = AccessToken.objects.get(pk=access_id)
        return access_token.check_token(input_token)
    except (ValidationError, AccessToken.DoesNotExist):
        return False


def check_access_id(access_id):
    try:
        access_token = AccessToken.objects.get(pk=access_id)
        return True
    except (ValidationError, AccessToken.DoesNotExist):
        return False
