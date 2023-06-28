from rest_framework import serializers
from .models import Game, Quote, Platform, Genre

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

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
GENRES_DICT = dict(GENRES_OPTIONS)


class GenreSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    raw_name = serializers.IntegerField(source='name')

    def get_name(self, obj):
        return GENRES_DICT.get(obj.name)

    class Meta:
        model = Genre
        fields = '__all__'

PLATFORMS_OPTIONS = [
    (1,'PC'),
    (2,'Xbox'),
    (3,'Playstation'),
    (4,'Switch'),
    (5,'All')
    ]

PLATFORMS_DICT = dict(PLATFORMS_OPTIONS)

class PlatformSerializer(serializers.ModelSerializer):
    
    name = serializers.SerializerMethodField()
    raw_name = serializers.IntegerField(source='name')
    
    def get_name(self, obj):
        return PLATFORMS_DICT.get(obj.name)
    
    class Meta:
        model = Platform
        fields = '__all__'