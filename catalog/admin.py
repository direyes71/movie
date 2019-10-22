from django.contrib import admin

from catalog.models import Director
from catalog.models import Genre
from catalog.models import Movie
from catalog.models import Rating


class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'year',
        'duration',
    )


admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating)
