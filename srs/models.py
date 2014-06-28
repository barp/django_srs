from django.db import models

from django.db import models

class Deck(models.Model):
    name = models.CharField(max_length=50)
    card_template = models.FileField()

class Card(models.Model):
    decks = models.ForeignKey(Deck)
    card_name = models.CharField(max_length=50)

class CardField(models.Model):
    deck = models.ForeignKey(Deck)
    field_name = models.CharField(max_length=50)

class CardFieldValue(models.Model):
    card = models.ForeignKey(Card)
    field = models.ForeignKey(CardField)
    value = models.CharField(max_length=500)

class LearningState(models.Model):
    parent_deck = models.ForeignKey(Deck)
    session_number = models.PositiveSmallIntegerField()

class LearningDeck(models.Model):
    learning_state = models.ForeignKey(LearningState)
    first_session = models.PositiveSmallIntegerField()
    CURRENT_DECK = "CUR"
    IN_PROGRESS_DECK = "PRO"
    RETIRED_DECK = "RET"
    DECK_TYPES = (
        (CURRENT_DECK, "Current Deck"),
        (IN_PROGRESS_DECK, "In Progress Deck"),
        (RETIRED_DECK, "Retired Deck")
    )
    deck_type = models.CharField(max_length=3, choices=DECK_TYPES, default=CURRENT_DECK)

class CardLearningInstance(models.Model):
    actual_card = models.ForeignKey(Card)
    current_learning_deck = models.ForeignKey(LearningDeck)
