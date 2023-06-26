from django.db import models
from django.contrib.auth.models import User

# Gêneros de jogos
# https://en.wikipedia.org/wiki/Video_game_genre

GENRES_OPTIONS = [
    (1, 'Ação'),
    (2, 'Aventura'),
    (3, 'Luta'),
    (4, 'Plataforma'),
    (5, 'Quebra-cabeça'),
    (6, 'Corrida'),
    (7, 'RPG'),
    (8, 'Tiro'),
    (9, 'Simulação'),
    (10, 'Esportes'),
    (11, 'Estratégia'),
    (12, 'MOBA')
    ]

PLATFORMS_OPTIONS = [
    (1,'PC'),
    (2,'Xbox'),
    (3,'Playstation'),
    (4,'Switch'),
    (5,'All')
    ]
    
PLAYERS_OPTIONS = [
    (1,'Single-player'),
    (2,'Multiplayer'),
    (3,'Ambos'),
    (4,'Melhor com amigos!')
    ]
    
CONNECTIVITY_OPTIONS = [
    (1,'Offline'),
    (2,'Online'),
    (3,'Ambos')
    ]

class Genre(models.Model):    
    name = models.IntegerField(choices=GENRES_OPTIONS)

class Platform(models.Model):
    name = models.IntegerField(choices=PLATFORMS_OPTIONS)

class Game(models.Model):    
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    platforms = models.ManyToManyField(Platform)
    players = models.IntegerField(choices=PLAYERS_OPTIONS, default=1)
    synopsis = models.TextField()
    connectivity = models.IntegerField(choices=CONNECTIVITY_OPTIONS, default=1)
    wiki = models.URLField()

class Quote(models.Model):
    phrase = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
