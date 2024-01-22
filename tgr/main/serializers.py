from rest_framework import serializers
from .models import Game, Quote, Platform, Genre, Players, Perspective
from .constants import GENRES_OPTIONS, PLATFORMS_OPTIONS, PLAYERS_OPTIONS, PERSPECTIVE_OPTIONS

GENRES_DICT = dict(GENRES_OPTIONS)
PLATFORMS_DICT = dict(PLATFORMS_OPTIONS)
PLAYERS_DICT = dict(PLAYERS_OPTIONS)
PERSPECTIVE_DICT = dict(PERSPECTIVE_OPTIONS)

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    raw_name = serializers.IntegerField(source='name')

    def get_name(self, obj):
        return GENRES_DICT.get(obj.name)

    class Meta:
        model = Genre
        fields = '__all__'

class PlatformSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    raw_name = serializers.IntegerField(source='name')
    
    def get_name(self, obj):
        return PLATFORMS_DICT.get(obj.name)
    
    class Meta:
        model = Platform
        fields = '__all__'

class PlayersSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField()
    raw_name = serializers.IntegerField(source='name')
    
    def get_name(self, obj):
        return PLAYERS_DICT.get(obj.name)
    
    class Meta:
        model = Players
        fields = '__all__'

class PerspectiveSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField()
    raw_name = serializers.IntegerField(source='name')
    
    def get_name(self, obj):
        return PERSPECTIVE_DICT.get(obj.name)
    
    class Meta:
        model = Perspective
        fields = '__all__'