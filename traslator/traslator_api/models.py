import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import TraslationManager


class Traslation(models.Model):
    SPLIT_CHAR = "||"
    REQUESTED = 1
    TRASLATED = 2
    FAILED = 3
    STATUSES = (
        (REQUESTED, _('REQUESTED')),
        (TRASLATED, _('TRASLATED')),
        (FAILED, _('FAILED')),
    )

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    lang_source = models.CharField(_('language source'), max_length=15,)
    lang_target = models.CharField(_('language target'), max_length=15,)
    text = models.TextField(_('text'))
    traslation = models.TextField("traslation", null=True)
    status = models.SmallIntegerField(
        _('status'), choices=STATUSES, default=REQUESTED, editable=False,)
    creation_time = models.DateTimeField(
        _("creation time"), auto_now=True, editable=False,)
    finish_time = models.DateTimeField(
        _("finish time"), editable=False, null=True,)

    objects = TraslationManager()

    class Meta:
        verbose_name = _('traslation')
        verbose_name_plural = _('traslations')

    def __str__(self):
        return "Traslation %s to %s" % (self.lang_source, self.lang_target)
