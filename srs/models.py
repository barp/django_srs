from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=50)
    card_template = models.FileField()

# Create your models here.
class Card(models.Model):
    decks = models.ManyToManyField(Deck)
    card_name = models.CharField(max_length=50)

class CardField(models.Model):
    deck = models.ForeignKey(Deck)
    field_name = models.CharField(max_length=50)

class CardFieldValue(models.Model):
    card = models.ForeignKey(Card)
    field = models.ForeignKey(CardField)
    value = models.CharField(max_length=500)

class CardLearningData(models.Model):
    card = models.ForeignKey(Card)
    proficiency_level = models.PositiveSmallIntegerField()