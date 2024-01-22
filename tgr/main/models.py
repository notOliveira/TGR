from django.db import models
from django.contrib.auth.models import User
from .constants import PLATFORMS_OPTIONS, GENRES_OPTIONS, PLAYERS_OPTIONS, PERSPECTIVE_OPTIONS #CONNECTIVITY_OPTIONS

class Genre(models.Model):
    name = models.IntegerField(choices=GENRES_OPTIONS)
    
    def __str__(self):
        return self.get_name_display()

class Platform(models.Model):
    name = models.IntegerField(choices=PLATFORMS_OPTIONS)
    
    def __str__(self):
        return self.get_name_display()
    
class Players(models.Model):
    name = models.IntegerField(choices=PLAYERS_OPTIONS)
    
    def __str__(self):
        return self.get_name_display()
    
class Perspective(models.Model):
    name = models.IntegerField(choices=PERSPECTIVE_OPTIONS)
    
    def __str__(self):
        return self.get_name_display()

class Game(models.Model):
    title = models.CharField(max_length=100)
    igdb_id = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    platforms = models.ManyToManyField(Platform)
    players_mode = models.ManyToManyField(Players)
    wiki = models.URLField()
    perspective = models.ManyToManyField(Perspective)
    # synopsis = models.TextField()
    # Esperar pela API do IGBD atualizar para adicionar esse campo
    # connectivity = models.IntegerField(choices=CONNECTIVITY_OPTIONS, default=1)

class Quote(models.Model):
    phrase = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
