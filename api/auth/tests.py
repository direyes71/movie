from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework.test import APITestCase


User = get_user_model()


class TestLoginCase(APITestCase):

    login_url = '/auth/login-token/'
    refresh_token_url = '/auth/refresh-token/'
    logout_url = '/auth/logout/'

    sign_up = '/auth/sign-up/'

    movie_url = '/catalog/movie/'

    username = 'test-user'
    password = 'movie-test'

    def setUp(self):
        self.user = User.objects.create_user(self.username, password=self.password, age=24, sex=1)
        self.client = APIClient()

    def test_login(self):
        data = {
            'username': self.username, 'password': self.password
        }
        response = self.client.post(self.login_url, data)
        body = response.json()
        if 'access' in body:
            self.client.credentials(
                HTTP_AUTHORIZATION='Bearer %s' % body['access'])
        return response.status_code, body

    def test_logout_response_204(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )
        response = self.client.post(self.logout_url)
        self.assertEquals(response.status_code, 204)

    def test_logout_with_not_login_response_401(self):
        response = self.client.post(self.logout_url)
        self.assertEquals(response.status_code, 401)

    def test_access_token_still_valid_after_logout(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )
        self.client.post(self.logout_url)
        response = self.client.get(self.movie_url)
        self.assertEquals(response.status_code, 401)

    def test_create_user(self):
        data = {
            'username': 'new-user-test',
            'password': 'new-user-test',
            'age': 24,
            'sex': 1,
        }
        response = self.client.post(self.sign_up, data)
        self.assertEquals(response.status_code, 201)
