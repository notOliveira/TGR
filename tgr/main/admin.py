from django.contrib import admin
from .models import Game, Quote, Genre, Players, Platform, Connectivity

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "get_genres_name",
        "get_platforms_name",
        "get_players_name",
        "get_connectivity_name",
        ]
    
    # Mostrando no Django Admin os campos que cada objeto tem
    
    # Connectivity
    def get_connectivity_name(self, obj):
        return ", ".join([connectivity.get_name_display() for connectivity in obj.connectivity.all()])

    get_connectivity_name.short_description = "Connectivity"
    
    # Players
    def get_players_name(self, obj):
        return ", ".join([players.get_name_display() for players in obj.players.all()])

    get_players_name.short_description = "Players"
    
    # Platforms
    def get_platforms_name(self, obj):
        return ", ".join([platforms.get_name_display() for platforms in obj.platforms.all()])

    get_platforms_name.short_description = "Platforms"
    
    # Genres
    def get_genres_name(self, obj):
        return ", ".join([genres.get_name_display() for genres in obj.genres.all()])

    get_genres_name.short_description = "Genres"

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "game_title", "phrase"]
    
    def game_title(self, obj):
        return obj.game.title

    game_title.short_description = "Game"

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):    
    list_display = ["id", "name"]

@admin.register(Players)
class PlayersAdmin(admin.ModelAdmin):    
    list_display = ["id", "name"]

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):    
    list_display = ["id", "name"]

@admin.register(Connectivity)
class ConnectivityAdmin(admin.ModelAdmin):    
    list_display = ["id", "name"]