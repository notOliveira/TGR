from django.core.management.base import BaseCommand
from main.models import Genre
from main.constants import GENRES_OPTIONS

class Command(BaseCommand):
    help = 'Cria objetos Genre'

    def handle(self, *args, **options):
        # Adiciona os gêneros
        Genre.objects.bulk_create([Genre(name=value) for value, _ in GENRES_OPTIONS if not Genre.objects.filter(name=value).exists()])

        self.stdout.write(self.style.SUCCESS('Gêneros criados com sucesso.'))