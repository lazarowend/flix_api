from movies.models import Movie
from movies.serializers import MovieModelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from reviews.models import Review
from rest_framework import status, response
from django.db.models import Count, Avg

class ListCreateMovieView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class RetrieveUpdateDestroyMovieView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MovieStatsView(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()

    def get(self, request):
        amount_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        amount_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']
        
        data = {
            'amount_movies': amount_movies,
            'movies_by_genre': movies_by_genre,
            'amount_reviews': amount_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0
        }
        
        return response.Response(
            data=data,
            status=status.HTTP_200_OK
        )
