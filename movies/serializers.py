from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg


class MovieModelSerializer(serializers.ModelSerializer):


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

