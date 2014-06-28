from django.contrib import admin
from srs.models import Deck, CardField

class CardFieldsAdmin(admin.TabularInline):
    model = CardField
    extra = 5

class DeckAdmin(admin.ModelAdmin):
    inlines = [CardFieldsAdmin]

admin.site.register(Deck, DeckAdmin)