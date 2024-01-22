from django.shortcuts import render # redirect
from django.views.generic import ListView, CreateView
from .models import Game, Quote, Platform, Genre, Perspective, Players
from .forms import GameForm
from rest_framework import viewsets, permissions
from .serializers import GameSerializer, QuoteSerializer, PlatformSerializer, GenreSerializer, PerspectiveSerializer, PlayersSerializer
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse # HttpResponseForbidden
# from django.contrib.auth.mixins import LoginRequiredMixin
import requests

def error_403(request):
    context = {'status': 403}
    return render(request, 'main/errors.html', context)

def error_403_api(request):
    return JsonResponse({'error': 'You are not authorized to access this page.'}, status=403)

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

@login_required
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

    payload = f"fields name, genres.name, platforms.name, player_perspectives.name, game_modes.name, url;where id = {game_id};"

    response = requests.post(igdb_url, headers=headers, data=payload)
    data = response.json()

    return JsonResponse(data, safe=False)
    
class CreateSuperUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return False
        return True

@method_decorator([login_required, user_passes_test(lambda u: u.is_superuser, login_url='error-403')], name='dispatch')
class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'main/add_game.html'
    success_url = '/add-game'

@method_decorator([login_required, user_passes_test(lambda u: u.is_superuser, login_url='error-403')], name='dispatch')
class GameListView(ListView):
    model = Game
    template_name = 'main/games.html'
    context_object_name = 'list-games'
    ordering = ['title']
    
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
    
class PerspectiveViewSet(viewsets.ModelViewSet):
    queryset = Perspective.objects.all()
    serializer_class = PerspectiveSerializer
    permission_classes = [CreateSuperUserPermission]

class PlayersViewSet(viewsets.ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
    permission_classes = [CreateSuperUserPermission]