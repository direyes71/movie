from django.db.models import Max
from django.db.models import Min

from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from api.catalog.serializers import NewMovieSerializer
from catalog.models import Movie
from catalog.models import Rating


class MovieViewSet(
        CreateModelMixin,
        RetrieveModelMixin,
        ListModelMixin,
        UpdateModelMixin,
        DestroyModelMixin,
        GenericViewSet,
        ):
    """
    retrieve:
        Return a movie instance.

    list:
        Return movie list.

        query_string params:
        - name
        - director
        - genre
        - best_movie (value=1)

    create:
        Create a new movie.

    delete:
        Remove an existing movie.

    update:
        Update a movie.
    """

    serializer_class = NewMovieSerializer
    queryset = Movie.objects.all().order_by('-stars')
    permission_classes = (AllowAny,)

    def filter_queryset(self, queryset):
        query = {}
        if u'name' in self.request.GET:
            query['name__icontains'] = self.request.GET['name']

        if u'director' in self.request.GET:
            query['director__name__icontains'] = self.request.GET['director']

        if u'genre' in self.request.GET:
            query['genre__name__icontains'] = self.request.GET['genre']

        if u'best_movie' in self.request.GET:
            query['stars__gte'] = 3

        return queryset.filter(**query)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        Rating.objects.filter(
            movie=instance,
        ).delete()
        return super(MovieViewSet, self).destroy(request, *args, **kwargs)

class BestMovieViewSet(
        ListModelMixin,
        GenericViewSet,
        ):
    """ Return the first best movies for specific user

    list:
        Return movie list.
    """

    serializer_class = NewMovieSerializer
    queryset = Movie.objects.all()

    def filter_queryset(self, queryset):
        gender = self.request.user.gender
        age = self.request.user.age
        queryset = get_recommended_movies(
            base_queryset=queryset.order_by('-stars'),
            gender=gender,
            age=age,
        )
        return queryset


def get_recommended_movies(base_queryset, gender, age):
    """ Function to return the best movies for specific user

    :param base_queryset: catalog.Movie
    :param gender: int
    :param age: int
    :return: queryset
    """

    def get_age_range(age):
        age_ranges = (
            (18, 25),
            (26, 30),
            (31, 35),
            (36, 40),
            (41, 45),
            (46, 50),
            (51, 55),
            (56, 60),
        )
        age_range = None

        for range in age_ranges:
            if age < range[0]:
                age_range = range
                break
            if range[0] <= age <= range[1]:
                age_range = range
                break
        if not age_range:
            age_range = age_ranges[-1]
        return age_range

    def get_movie_list(gender, age):
        movies = base_queryset.filter(
            rating__created_by__gender=gender,
            rating__created_by__age=age,
        ).distinct()
        if not movies.exists():
            movies = base_queryset.filter(
                rating__created_by__age=age,
            ).distinct()
            if not movies.exists():
                max_age = base_queryset.aggregate(max_age=Max('rating__created_by__age'))['max_age']
                min_age = base_queryset.aggregate(min_age=Min('rating__created_by__age'))['min_age']
                age = max_age if max_age < age else min_age
                movies = base_queryset.filter(
                    rating__created_by__age=age,
                )
        return movies

    movies = get_movie_list(gender=gender, age=age)
    return movies[:5]
