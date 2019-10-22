from django.utils.translation import ugettext_lazy as _


VERY_BAD = 1
BAD = 2
REGULAR = 3
GOOD = 4
VERY_GOOD = 5

RATING_CHOICES = (
    (VERY_BAD, _(u'very bad')),
    (BAD, _(u'bad')),
    (REGULAR, _(u'regular')),
    (GOOD, _(u'good')),
    (VERY_GOOD, _(u'very good')),
)
