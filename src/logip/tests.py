import json

from django.contrib.auth.models import User
from django.test import Client, TestCase

from .models import AccessToken


class NoDataTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        user = User.objects.create_user(username='django')
        access_token = AccessToken.objects.create(user=user)
        self.access_id = str(access_token.pk)
        self.token = access_token.gen_token()

    def test_no_data_request(self):
        response1 = self.client.get('/')
        self.assertEqual(response1.status_code, 403)
        response2 = self.client.get('/update/')
        self.assertEqual(response2.status_code, 403)

        response3 = self.client.get('/update/?ip=%s&access_id=%s&access_token=%s' % ('1.1.1.1', self.access_id, self.token))
        self.assertEqual(response3.status_code, 200)
        response4 = self.client.get('/?access_id=%s' % self.access_id)
        response_dict = response4.json()
        self.assertEqual(response_dict['ip'], '1.1.1.1')

        response5 = self.client.get('/update/?ip=%s&access_id=%s&access_token=%s' % ('1.1.1.1', self.access_id, self.token))
        self.assertEqual(response5.status_code, 200)
        response6 = self.client.get('/?access_id=%s' % self.access_id)
        self.assertEqual(response4.json(), response6.json())

        response7 = self.client.get('/update/?ip=%s&access_id=%s&access_token=%s' % ('1.1.1.2', self.access_id, self.token))
        self.assertEqual(response7.status_code, 200)
        response_dict7 = response7.json()
        self.assertEqual(response_dict7['ip'], '1.1.1.2')
