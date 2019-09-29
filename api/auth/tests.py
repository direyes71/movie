from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework.test import APITestCase


class TestLoginCase(APITestCase):

    factory = APIClient()

    login_url = '/auth/login-token/'
    refresh_token_url = '/auth/refresh-token/'
    logout_url = '/auth/logout/'

    movie_url = '/catalog/movie/'

    username = 'test-user'
    password = 'movie-test'

    def setUp(self):
        self.user = User.objects.create_user(self.username, password=self.password)

    def test_login(self):
        data = {
            'username': self.username, 'password': self.password
        }
        r = self.client.post(self.login_url, data)
        body = r.json()
        if 'access' in body:
            self.client.credentials(
                HTTP_AUTHORIZATION='Bearer %s' % body['access'])
        return r.status_code, body

    def test_logout_response_204(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )
        response = self.client.post(self.logout_url)
        self.assertEquals(response.status_code, 204)

    def test_logout_with_not_login_response_401(self):
        r = self.client.post(self.logout_url)
        self.assertEquals(r.status_code, 401)

    def test_access_token_still_valid_after_logout(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )
        self.client.post(self.logout_url)
        r = self.client.get(self.movie_url)
        self.assertEquals(r.status_code, 401)
