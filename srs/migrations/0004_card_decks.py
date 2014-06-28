# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srs', '0003_cardlearningdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='decks',
            field=models.ManyToManyField(to=b'srs.Deck'),
            preserve_default=True,
        ),
    ]
