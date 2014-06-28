# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srs', '0003_auto_20140628_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='card_back_template',
            field=models.FileField(upload_to=b''),
        ),
    ]
