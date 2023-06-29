from django.shortcuts import render
from django.views.generic import ListView
from .models import Game, Quote, Platform, Genre
from rest_framework import viewsets, permissions
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

class CreateSuperUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.is_superuser
        return True

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [CreateSuperUserPermission]

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [CreateSuperUserPermission]
    
class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [CreateSuperUserPermission]

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [CreateSuperUserPermission]
