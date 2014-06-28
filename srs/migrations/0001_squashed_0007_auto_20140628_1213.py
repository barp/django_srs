# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [(b'srs', '0001_initial'), (b'srs', '0002_auto_20140628_1038'), (b'srs', '0003_cardlearningdata'), (b'srs', '0004_card_decks'), (b'srs', '0005_auto_20140628_1208'), (b'srs', '0006_auto_20140628_1209'), (b'srs', '0007_auto_20140628_1213')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('card_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CardField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('card_template', models.FileField(upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cardfield',
            name='deck',
            field=models.ForeignKey(to='srs.Deck'),
            preserve_default=True,
        ),
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
        migrations.AddField(
            model_name='card',
            name='decks',
            field=models.ManyToManyField(to=b'srs.Deck'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='CardLearningInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actual_card', models.ForeignKey(to='srs.Card')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LearningDeck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_session', models.PositiveSmallIntegerField()),
                ('deck_type', models.CharField(default=b'CUR', max_length=3, choices=[(b'CUR', b'Current Deck'), (b'PRO', b'In Progress Deck'), (b'RET', b'Retired Deck')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cardlearninginstance',
            name='current_learning_deck',
            field=models.ForeignKey(to='srs.LearningDeck'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='LearningState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_number', models.PositiveSmallIntegerField()),
                ('parent_deck', models.ForeignKey(to='srs.Deck')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='learningdeck',
            name='learning_state',
            field=models.ForeignKey(to='srs.LearningState'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='decks',
            field=models.ForeignKey(to='srs.Deck'),
        ),
    ]
