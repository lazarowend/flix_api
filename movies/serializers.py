from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg
from actors.serializers import ActorModelSerializer
from genres.serializers import GenreModelSerializer


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_realeade_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990.')
        return value

    def get_rate(self, obj):
        rate = obj.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return rate

        return None


class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorModelSerializer(many=True)
    genre = GenreModelSerializer()
    rate = serializers.IntegerField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return rate

        return None
