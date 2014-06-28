# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srs', '0002_auto_20140628_1038'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardLearningData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proficiency_level', models.PositiveSmallIntegerField()),
                ('card', models.ForeignKey(to='srs.Card')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
