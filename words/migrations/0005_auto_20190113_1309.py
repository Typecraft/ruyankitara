# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-01-13 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0004_auto_20170919_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='augment',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='word',
            name='POS',
            field=models.CharField(blank=True, default='', max_length=31),
        ),
        migrations.AlterField(
            model_name='word',
            name='dialect',
            field=models.CharField(blank=True, default='', max_length=127),
        ),
        migrations.AlterField(
            model_name='word',
            name='gloss',
            field=models.CharField(blank=True, default='', max_length=127),
        ),
        migrations.AlterField(
            model_name='word',
            name='no',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='note',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='word',
            name='prefix',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='word',
            name='tone',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(blank=True, default='', max_length=511),
        ),
        migrations.AlterField(
            model_name='word',
            name='word_class',
            field=models.CharField(blank=True, default='', max_length=31),
        ),
    ]
