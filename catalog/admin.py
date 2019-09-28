from django.contrib import admin

from catalog.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'year',
        'duration',
    )


admin.site.register(Movie, MovieAdmin)
