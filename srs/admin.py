from django.contrib import admin
from srs.models import Deck, CardField, Card, CardFieldValue
import django.forms as forms

class CardFieldsAdmin(admin.TabularInline):
    model = CardField
    extra = 5

class DeckAdmin(admin.ModelAdmin):
    inlines = [CardFieldsAdmin]

class CardFieldValueAdmin(admin.TabularInline):
    model = CardFieldValue
    extra = 5

class CardAdmin(admin.ModelAdmin):
    inlines = [CardFieldValueAdmin]

admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)