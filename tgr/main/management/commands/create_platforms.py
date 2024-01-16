from django.core.management.base import BaseCommand
from main.models import Game, Platform
from main.constants import PLATFORMS_OPTIONS

class Command(BaseCommand):
    help = 'Cria objetos Platform e os associa aos jogos existentes'

    def handle(self, *args, **options):
        # Adiciona as plataformas
        Platform.objects.bulk_create([Platform(name=name) for _, name in PLATFORMS_OPTIONS])

        # Associa as plataformas aos jogos existentes
        for jogo in Game.objects.all():
            jogo.platforms.add(*Platform.objects.all())

        self.stdout.write(self.style.SUCCESS('Plataformas e associações criadas com sucesso.'))