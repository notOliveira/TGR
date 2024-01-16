from django.core.management.base import BaseCommand
from main.models import Platform
from main.constants import PLATFORMS_OPTIONS

class Command(BaseCommand):
    help = 'Cria objetos Platform'

    def handle(self, *args, **options):
        # Adiciona as plataformas
        Platform.objects.bulk_create([Platform(name=value) for value, _ in PLATFORMS_OPTIONS if not Platform.objects.filter(name=value).exists()])

        self.stdout.write(self.style.SUCCESS('Plataformas criadas com sucesso.'))