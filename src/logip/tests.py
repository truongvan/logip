import json

from django.test import Client, TestCase


class NoDataTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_no_data_request(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class UpdateRecordTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def update_record(self):
        response = self.client.get('/update/')
        self.assertEqual(response.status_code, 200)

    def view_record(self):
        response = self.client.get('/')
        response_dict = json.loads(response)
        self.assertEqual(response_dict.ip, '127.0.0.1')
