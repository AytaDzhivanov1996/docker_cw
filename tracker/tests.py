from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User(email='ayta@sky.pro')
        self.user.set_password('qwe123rty456')
        self.user.save()

        response = self.client.post("/users/api/token/", {"email": "ayta@sky.pro", "password": "qwe123rty456"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_my_habit_list(self):
        response = self.client.get('/tracker/my_habit_list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_public_habit_list(self):
        response = self.client.get('/tracker/public_habit_list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_habit(self):
        data_for_response = {
            "place": "Дом",
            "time": "13:00",
            "action": "eat some candies",
            "pleasant": "True",
            "time_to_complete": "00:02:00",
            "frequency": "1"
        }
        response = self.client.post('/tracker/create_habit/', data_for_response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_habit(self):
        data_for_response = {
            "place": "Дом",
            "time": "13:00",
            "action": "eat some candies",
            "pleasant": "True",
            "time_to_complete": "00:02:00",
            "frequency": "1"
        }
        response = self.client.put(f'/tracker/update_habit/1/', data_for_response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_habit(self):
        response = self.client.get(f'/tracker/retrieve_habit/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        response = self.client.delete(f'/tracker/destroy_habit/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
