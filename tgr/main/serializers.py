from rest_framework import serializers
from .models import Game, Quote, Platform, Genre
from .constants import GENRES_OPTIONS, PLATFORMS_OPTIONS

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

GENRES_DICT = dict(GENRES_OPTIONS)


class GenreSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    raw_name = serializers.IntegerField(source='name')

    def get_name(self, obj):
        return GENRES_DICT.get(obj.name)

    class Meta:
        model = Genre
        fields = '__all__'

PLATFORMS_DICT = dict(PLATFORMS_OPTIONS)

class PlatformSerializer(serializers.ModelSerializer):
    
    name = serializers.SerializerMethodField()
    raw_name = serializers.IntegerField(source='name')
    
    def get_name(self, obj):
        return PLATFORMS_DICT.get(obj.name)
    
    class Meta:
        model = Platform
        fields = '__all__'