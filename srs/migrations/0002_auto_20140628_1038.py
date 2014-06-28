# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardFieldValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=500)),
                ('card', models.ForeignKey(to='srs.Card')),
                ('field', models.ForeignKey(to='srs.CardField')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='cardfieldsvalue',
            name='card',
        ),
        migrations.RemoveField(
            model_name='cardfieldsvalue',
            name='field',
        ),
        migrations.DeleteModel(
            name='CardFieldsValue',
        ),
    ]
