from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=1000)
    wordExample = models.CharField(max_length=1000)
    freeTrans = models.CharField(max_length=1000, default="")
    freeTransExample = models.CharField(max_length=1000, default="")
    freeTrans2 = models.CharField(max_length=1000, default="")
    freeTrans2Example = models.CharField(max_length=1000, default="")

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s => %s" % (self.word, self.freeTrans)
