from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from userprofile.choices import SEX_CHOICES


class Profile(AbstractUser):
    """ Model for users
    """

    age = models.PositiveIntegerField(
        null=True,
        verbose_name=_(u'age'),
    )
    sex = models.PositiveIntegerField(
        null=True,
        choices=SEX_CHOICES,
        verbose_name=_(u'sex'),
    )
