from django.db import models
from django.urls import reverse

# Create your models here.

GENRES_OPTIONS = [
    (1, 'Action'),
    (2, 'Adventure'),
    (3, 'RPG'),
    (4, 'Strategy'),
    (5, 'Sports'),
    (6, 'Simulation'),
    (7, 'Puzzle'),
    (8, 'Racing'),
    (9, 'Shooter'),
    (10, 'Fighting'),
    (11, 'MOBA'),
    (12, 'Real-time Strategy'),
    (13, 'Visual Novel'),
    (14, 'Terror'),
    (15, 'Beat \'em up'),
    (16, 'Platformer'),
    (17, 'Card game'),
    (18, 'Board game'),
    (19, 'Graphic adventure'),
    (20, 'Stealth'),
    (21, 'Interactive fiction'),
    (22, 'Turn-based strategy'),
    (23, 'Sandbox'),
    (24, 'Construction game'),
    (25, 'Roguelike'),
    (26, 'Metroidvania'),
    (27, 'Battle royale'),
    (28, 'Hack and slash'),
    (29, 'Rhythm game'),
    (30, 'Educational game'),
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