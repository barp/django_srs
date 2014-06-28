# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srs', '0005_auto_20140628_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardlearningdata',
            name='card',
        ),
        migrations.DeleteModel(
            name='CardLearningData',
        ),
    ]
