from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from django.contrib.auth.models import User


class BookingSystemTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("aswin", "aswin@test,com", "pass-1234")
        self.client = APIClient()
        self.login_url = reverse("login")
        self.hello_url = reverse("hello-world")
        self.user_url = reverse("user-info")
        self.access_token = self.client.post(
            self.login_url, {"username": "aswin", "password": "pass-1234"}
        ).json()["access"]

    def test_login_return_jwt(self):
        credentials = {
            "username": "aswin",
            "password": "pass-1234",
        }

        response = self.client.post(self.login_url, credentials)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("access" in response.json().keys())
        self.assertTrue("refresh" in response.json().keys())

    def test_helloworld(self):

        expected_response = {"message": "Hello World"}
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)
        response = self.client.get(self.hello_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_response)
