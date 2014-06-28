# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srs', '0002_auto_20140628_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='card_back_template',
            field=models.FileField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='deck',
            old_name='card_template',
            new_name='card_front_template',
        ),
    ]
