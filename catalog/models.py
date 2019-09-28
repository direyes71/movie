from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.django.db.models import Auditor


class Movie(Auditor):
    """ Model for Movie
    """

    title = models.CharField(
        max_length=340,
        verbose_name=_(u'title'),
    )
    duration = models.PositiveIntegerField(
        default=0,
        verbose_name=_(u'duration'),
        help_text=_(u'Duration in minutes'),
    )
    year = models.PositiveIntegerField(
        null=True,
        verbose_name=_(u'year'),
    )

    def __str__(self):
        return self.movie_title
