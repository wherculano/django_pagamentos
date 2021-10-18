from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User

from pages.views import ClientViewSet, BillsViewSet


class AuthenticatorTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', email='tester@mail.com', password='1234!@#$')
        self.client = APIClient()
        self.login_url = reverse('token_obtain_pair')
        self.access_token = self.client.post(self.login_url,
                                             {"username": "tester", "password": "1234!@#$"}).json()['access']

    def test_token_jwt_ok(self):
        credentials = {
            "username": "tester",
            "password": "1234!@#$"
        }
        response = self.client.post(self.login_url, credentials)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('access' in response.json().keys())
        self.assertTrue('refresh' in response.json().keys())

    def test_token_jwt_not_ok(self):
        credentials = {
            "username": "tester",
            "password": "1234"
        }
        response = self.client.post(self.login_url, credentials)
        self.assertEqual(response.status_code, 401)

    def test_clientviewset(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.get('/client/')
