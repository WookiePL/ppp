# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0003_auto_20171210_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poem',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poems.Author'),
        ),
    ]