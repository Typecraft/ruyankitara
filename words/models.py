from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Word(models.Model):
    word = models.CharField(blank=True, default="", max_length=511)
    prefix = models.CharField(blank=True, default="", max_length=255)
    augment = models.CharField(blank=True, default="", max_length=255)
    stem = models.CharField(default="", max_length=255)
    tone = models.CharField(blank=True, default="", max_length=255)
    POS = models.CharField(blank=True, default="", max_length=31)
    word_class = models.CharField(blank=True, default="", max_length=31)
    gloss = models.CharField(blank=True, default="", max_length=127)
    no = models.IntegerField(blank=True, unique=True, null=True)
    note = models.TextField(blank=True, default="")
    dialect = models.CharField(blank=True, default="", max_length=127)

    def __unicode__(self):
        return u"%s" % (self.word,)
