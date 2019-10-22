import json

from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from catalog.models import Movie
from catalog.models import Rating


User = get_user_model()


class ServicesTestCase(TestCase):
    username = 'test-user'
    password = 'movie-test'

    def setUp(self):
        self.user = User.objects.create_user(self.username, password=self.password, age=24, gender=1)

        self.client = APIClient()

        self.client.login(
            username=self.username,
            password=self.password,
        )

    def _create_movie(self):
        name = u'movie-tittle-test'
        duration = 240
        year = 2012
        stars = 4
        genre = u'action-test'
        director = u'director-test'
        data = {
            'name': name,
            'duration': duration,
            'year': year,
            'stars': stars,
            'genre': genre,
            'director': director,
        }
        response = self.client.post(
            '/catalog/movie/',
            data,
        )
        movie = Movie.objects.last()

        Rating.objects.create(
            rate=4.0,
            created_by=self.user,
            movie=movie,
        )

        return movie

    def test_create_movie(self):
        initial_movies = Movie.objects.count()
        name = u'movie-tittle-test'
        duration = 240
        year = 2012
        stars = 4
        genre = u'action-test'
        director = u'director-test'
        data = {
            'name': name,
            'duration': duration,
            'year': year,
            'stars': stars,
            'genre': genre,
            'director': director,
        }
        response = self.client.post(
            '/catalog/movie/',
            data,
        )

        # Validate status of request
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Validate movies on database
        self.assertEquals(Movie.objects.count(), initial_movies + 1)

        # Validate data
        movie = Movie.objects.last()
        self.assertEqual(movie.name, name)
        self.assertEqual(movie.duration, duration)
        self.assertEqual(movie.year, year)
        self.assertEqual(movie.stars, stars)
        self.assertEqual(movie.genre.name, genre)
        self.assertEqual(movie.director.name, director)

    def test_retrieve_movie(self):
        _movie = self._create_movie()
        url = '/catalog/movie/{0}/'.format(_movie.id)
        response = self.client.get(
            url,
        )

        # Validate status of request
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = json.loads(response.content)

        # Validate data
        self.assertEqual(data['id'], _movie.id)
        self.assertEqual(data['name'], _movie.name)
        self.assertEqual(data['duration'], _movie.duration)
        self.assertEqual(data['year'], _movie.year)
        self.assertEqual(data['stars'], _movie.stars)
        self.assertEqual(data['genre'], _movie.genre.name)
        self.assertEqual(data['director'], _movie.director.name)
        self.assertEqual(data['name'], _movie.__str__())

    def test_retrieve_movie_list(self):
        _movie = self._create_movie()
        url = '/catalog/movie/'
        response = self.client.get(
            url,
        )

        # Validate status of request
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = json.loads(response.content)
        movies = data['results']

        # Validate data
        self.assertEqual(len(movies), Movie.objects.count())

    def test_update_movie(self):
        original_movie = self._create_movie()
        name = u'movie-tittle-test-updated'
        duration = 280
        year = 2014
        stars = 5
        genre = u'action-test-updated'
        director = u'director-test-updated'
        data = {
            'name': name,
            'duration': duration,
            'year': year,
            'stars': stars,
            'genre': genre,
            'director': director,
        }
        url = '/catalog/movie/{0}/'.format(original_movie.id)
        response = self.client.put(
            url,
            data,
        )

        # Validate status of request
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Validate data
        movie = Movie.objects.get(id=original_movie.id)
        self.assertEqual(movie.name, name)
        self.assertEqual(movie.duration, duration)
        self.assertEqual(movie.year, year)
        self.assertEqual(movie.stars, stars)
        self.assertEqual(movie.genre.name, genre)
        self.assertEqual(movie.director.name, director)

    def test_delete_movie(self):
        original_movie = self._create_movie()
        url = '/catalog/movie/{0}/'.format(original_movie.id)
        response = self.client.delete(
            url,
        )

        # Validate status of request
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Valdiate data
        self.assertFalse(Movie.objects.filter(id=original_movie.id).exists())

    def test_retrieve_movie_list_search(self):
        _movie = self._create_movie()
        url = '/catalog/movie/?name=movie-tittle-test&director=director-test&genre=action-test'
        response = self.client.get(
            url,
        )

        # Validate status of request
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = json.loads(response.content)
        movies = data['results']

        # Validate data
        self.assertEqual(len(movies), 1)

    def test_retrieve_movie_list_recommended(self):
        _movie = self._create_movie()
        url = '/catalog/movie/?best_movie=1'
        response = self.client.get(
            url,
        )

        # Validate status of request
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = json.loads(response.content)
        movies = data['results']

        # Validate data
        self.assertEqual(len(movies), 1)

    def test_age_range_retrieve_movie_list_recommended_by_specific_user(self):
        from api.catalog.views import get_recommended_movies
        _movie = self._create_movie()
        get_recommended_movies(Movie.objects.all(), 1, 24)

    def test_retrieve_movie_list_recommended_by_specific_user(self):
        _movie = self._create_movie()
        url = '/catalog/best-movie/'
        response = self.client.get(
            url,
        )

        # Validate status of request
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = json.loads(response.content)
        movies = data['results']

        # Validate data
        self.assertEqual(len(movies), 1)

    def test_rating_str(self):
        _movie = self._create_movie()
        rating = Rating.objects.get()
        self.assertEqual(
            rating.__str__(),
            u'{0}-{1}'.format(
                rating.movie.name,
                rating.rate,
            ),
        )
