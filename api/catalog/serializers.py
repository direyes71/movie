from rest_framework import serializers

from catalog.models import Director
from catalog.models import Genre
from catalog.models import Movie


class NewMovieSerializer(serializers.ModelSerializer):
    genre = serializers.CharField(max_length=240)
    director = serializers.CharField(max_length=340)

    class Meta:
        model = Movie
        fields = (
            'id',
            'name',
            'duration',
            'year',
            'stars',
            'genre',
            'director',
        )

    def validate_director(self, value):
        director, created = Director.objects.get_or_create(
            name=value,
            defaults={
                'created_by': self.context['request'].user,
            }
        )
        return director

    def validate_genre(self, value):
        genre, created = Genre.objects.get_or_create(
            name=value,
            defaults={
                'created_by': self.context['request'].user,
            }
        )
        return genre

    def create(self, validated_data):
        return Movie.objects.create(
            created_by=self.context['request'].user,
            **validated_data,
        )
