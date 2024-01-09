from django.db import models
from django.contrib.auth.models import User
from .constants import PLATFORMS_OPTIONS, GENRES_OPTIONS, PLAYERS_OPTIONS, CONNECTIVITY_OPTIONS

# Gêneros de jogos
# https://en.wikipedia.org/wiki/Video_game_genre

class Genre(models.Model):
    name = models.IntegerField(choices=GENRES_OPTIONS)
    
    def __str__(self):
        return self.get_name_display()

class Platform(models.Model):
    name = models.IntegerField(choices=PLATFORMS_OPTIONS)
    
    def __str__(self):
        return self.get_name_display()

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
