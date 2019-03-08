import dj_database_url
import django_heroku

from .base import *

DEBUG = False

DATABASES['default'] = dj_database_url.config(os.environ['DATABASE_URL'], conn_max_age=600)
django_heroku.settings(locals())
