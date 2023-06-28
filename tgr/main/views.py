from django.shortcuts import render
from django.views.generic import ListView
from .models import Game, Quote, Platform, Genre
from rest_framework import viewsets
from .serializers import GameSerializer, QuoteSerializer, PlatformSerializer, GenreSerializer
# from .forms import GameForm
# from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    randomQuote = Quote.objects.order_by('?').first()
    
    context = {
        "randomQuote": randomQuote,
        "gameTitle": randomQuote.game.title,
        "gameWiki": randomQuote.game.wiki,
    }    
    return render(request, 'main/home.html', context)

def about(request):  
    context = {
        'footer': True
    }    
    return render(request, 'main/about.html', context)

class jogosListView(ListView):
    model = Game
    template_name = 'main/games.html'
    context_object_name = 'games'
    ordering = ['title']

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    
class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
