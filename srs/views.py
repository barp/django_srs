from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from srs.models import Deck, Card


class IndexView(generic.ListView):
    template_name = 'srs/deck_index.html'
    context_object_name = 'decks_list'

    def get_queryset(self):
        return  Deck.objects.all()


class DeckView(generic.DetailView):
    model = Deck
    template_name = "srs/deck_detail.html"


class CardView(generic.DetailView):
    model = Card
    template_name = "srs/card_detail.html"

def new_card(request, pk):
    return HttpResponse("test")