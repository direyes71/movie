from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Auditor(models.Model):
    """ Abstract class to save logs
    """

    created_date = models.DateTimeField(
        auto_now_add=True,
        help_text=_('Creation date'),
    )
    created_by = models.ForeignKey(
        get_user_model(),
        related_name='%(class)s_created_by',
        help_text=_('Created by'),
        on_delete=models.CASCADE,
    )
    updated_date = models.DateTimeField(
        null=True,
        auto_now=True,
        help_text=_('Updated at'),
    )
    updated_by = models.ForeignKey(
        get_user_model(),
        null=True,
        related_name='%(class)s_updated_by',
        help_text=_('Updated by'),
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True
