from django.db import models

# Gêneros de jogos
# https://en.wikipedia.org/wiki/Video_game_genre

GENRES_OPTIONS = [
    (1, 'Action'),
    (2, 'Adventure'),
    (3, 'Fighting'),
    (4, 'Platform'),
    (5, 'Puzzle'),
    (6, 'Racing'),
    (7, 'RPG'),
    (8, 'Shooter'),
    (9, 'Simulation'),
    (10, 'Sports'),
    (11, 'Strategy'),
    (12, 'MOBA'),
    ]

PLATFORMS_OPTIONS = [
    (1,'PC'),
    (2,'Xbox'),
    (3,'Playstation'),
    (4,'Switch'),
    (5,'All')
    ]
    
NUM_PLAYERS = [
    (1,'Single player'),
    (2,'Multiplayer'),
    (3,'Both'),
    (4,'Better with friends!')
    ]
    
ON_OFF_BOTH = [
    (1,'Offline'),
    (2,'Online'),
    (3,'Both')
    ]

class Genre(models.Model):    
    name = models.IntegerField(choices=GENRES_OPTIONS)

class Platform(models.Model):
    name = models.IntegerField(choices=PLATFORMS_OPTIONS)

class Players(models.Model):
    name = models.IntegerField(choices=NUM_PLAYERS)

class Connectivity(models.Model):
    name = models.IntegerField(choices=ON_OFF_BOTH)
    
class Game(models.Model):    
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    platforms = models.ManyToManyField(Platform)
    players = models.ManyToManyField(Players)
    synopsis = models.CharField(max_length=300, default='')
    connectivity = models.ManyToManyField(Connectivity)
    wiki = models.URLField()

class Quote(models.Model):
    phrase = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class Quiz(models.Model):
    genres = models.ManyToManyField(Genre)
    platforms = models.ManyToManyField(Platform)
    players = models.ManyToManyField(Players)
    connectivity = models.ManyToManyField(Connectivity)