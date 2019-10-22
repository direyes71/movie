from django.db import models
from django.utils.translation import ugettext_lazy as _

from catalog.choices import RATING_CHOICES
from utils.django.db.models import Auditor


class Genre(Auditor):
    name = models.CharField(
        max_length=240,
        verbose_name=_(u'name'),
    )

    def __str__(self):
        return self.name


class Director(Auditor):
    name = models.CharField(
        max_length=340,
        verbose_name=_(u'name'),
    )

    def __str__(self):
        return self.name


class Movie(Auditor):
    """ Model for Movie
    """

    name = models.CharField(
        max_length=340,
        verbose_name=_(u'name'),
    )
    duration = models.PositiveIntegerField(
        default=0,
        verbose_name=_(u'duration'),
        help_text=_(u'Duration in minutes'),
    )
    year = models.PositiveIntegerField(
        null=True,
        verbose_name=_(u'Year'),
    )
    stars = models.FloatField(
        default=0,
        verbose_name=_(u'stars'),
    )
    genre = models.ForeignKey(
        'catalog.Genre',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_(u'Genre'),
    )
    director = models.ForeignKey(
        'catalog.Director',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_(u'Director'),
    )

    def __str__(self):
        return self.name


class Rating(Auditor):
    """ Model for Rating
    """

    rate = models.PositiveIntegerField(
        choices=RATING_CHOICES,
        verbose_name=_(u'rate'),
    )
    movie = models.ForeignKey(
        'catalog.Movie',
        null=True,
        on_delete=models.PROTECT,
        verbose_name=_(u'movie'),
    )

    def __str__(self):
        return u'{0}-{1}'.format(
            self.movie.name,
            self.rate,
        )
