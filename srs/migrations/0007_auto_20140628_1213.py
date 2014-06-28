# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srs', '0006_auto_20140628_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='decks',
            field=models.ForeignKey(to='srs.Deck'),
        ),
    ]
