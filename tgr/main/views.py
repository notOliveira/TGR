from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Game, Quote, Platform, Genre
from .forms import GameForm
from rest_framework import viewsets, permissions
from .serializers import GameSerializer, QuoteSerializer, PlatformSerializer, GenreSerializer
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
import requests

# from .forms import GameForm
# from django.contrib.auth.mixins import LoginRequiredMixin

def error_403(request):
    context = {'status': 403}
    return render(request, 'main/errors.html', context)

def error_403_api(request):
    return HttpResponseForbidden('Acesso negado, você não é um administrador.')

def home(request):
    randomQuote = Quote.objects.order_by('?').first() if Quote.objects.exists() else None
    context = {}
    
    if randomQuote:
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

# Verifica se o usuário é superuser, se não for, redireciona para a página de erro 403
@user_passes_test(lambda u: u.is_superuser, login_url='error-403')
def add_game(request):
    return render(request, 'main/add_game.html')

@user_passes_test(lambda u: u.is_superuser, login_url='error-403')
def admin_panel(request):
     return render(request, 'main/admin_panel.html')

@user_passes_test(lambda u: u.is_superuser, login_url='error_403_api')
def get_igdb_game(request, game_id):
    bearerToken = "zq1zt7ugzio7tqv43sbxfyz10huc4e"
    clientId = "lqgjwpeowsz5u90rmitxccrjw4elrl"
    clientSecret = "qkg2wjzyv7n348o2hxiwz20lg7rk0c"
    igdb_url = 'https://api.igdb.com/v4/games'
    
    headers = {
        'Accept': 'application/json',
        'Client-ID': f'{clientId}',
        'Client-Secret': f'{clientSecret}',
        'Authorization': f'Bearer {bearerToken}',
    }

    payload = f"fields name, genres, platforms, player_perspectives, first_release_date, multiplayer_modes, similar_games, summary, websites, url;where id = {game_id};"

    response = requests.post(igdb_url, headers=headers, data=payload)
    data = response.json()

    return JsonResponse(data, safe=False)

class GameListView(ListView):
    model = Game
    template_name = 'main/games.html'
    context_object_name = 'list-games'
    ordering = ['title']
    
class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'main/add_game.html'
    success_url = '/add-game'
    
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
