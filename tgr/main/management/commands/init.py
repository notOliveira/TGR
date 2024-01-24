from django.core.management.base import BaseCommand
from main.models import Players, Platform, Genre, Perspective
from main.constants import PLAYERS_OPTIONS, PLATFORMS_OPTIONS, GENRES_OPTIONS, PERSPECTIVE_OPTIONS

class Command(BaseCommand):
    help = 'Cria os objetos padrão do banco'
    
    def handle(self, *args, **options):
        
        # Adiciona os players
        Players.objects.bulk_create([Players(name=value) for value, _ in PLAYERS_OPTIONS if not Players.objects.filter(name=value).exists()])
        
        # Adiciona as plataformas
        Platform.objects.bulk_create([Platform(name=value) for value, _ in PLATFORMS_OPTIONS if not Platform.objects.filter(name=value).exists()])
        
        # Adiciona os gêneros
        Genre.objects.bulk_create([Genre(name=value) for value, _ in GENRES_OPTIONS if not Genre.objects.filter(name=value).exists()])
        
        # Adiciona as perspectivas
        Perspective.objects.bulk_create([Perspective(name=value) for value, _ in PERSPECTIVE_OPTIONS if not Perspective.objects.filter(name=value).exists()])
        
        self.stdout.write(self.style.SUCCESS('Objetos criados com sucesso.'))