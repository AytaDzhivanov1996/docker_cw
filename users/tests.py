from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User(email='ayta@sky.pro')
        self.user.set_password('qwe123rty456')
        self.user.save()

        response = self.client.post("/users/api/token/", {"email": "ayta@sky.pro", "password": "qwe123rty456"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_create_user(self):
        response = self.client.post(path="/users/create_user/",
                                    data={"email": "ayta3000@sky.pro", "password": "123qwe456rty"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
