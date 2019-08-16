from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from logip.models import AccessToken


class Command(BaseCommand):
    help = 'Create new user, create new accesstoken'

    def handle(self, *args, **options):
        user, _ = User.objects.get_or_create(username='logip')
        access_token, _ = AccessToken.objects.get_or_create(user=user)
        access_id = str(access_token.pk)
        token = access_token.gen_token()
        print("Access ID: {}".format(access_id))
        print("Token: {}".format(token))
