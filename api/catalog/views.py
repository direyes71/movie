from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import DestroyModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from api.catalog.serializers import NewMovieSerializer
from catalog.models import Movie


class MovieViewSet(
        CreateModelMixin,
        RetrieveModelMixin,
        ListModelMixin,
        UpdateModelMixin,
        DestroyModelMixin,
        GenericViewSet,
        ):

    serializer_class = NewMovieSerializer
    queryset = Movie.objects.all()

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
