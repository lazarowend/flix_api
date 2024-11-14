from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializers import MovieModelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateMovieView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class RetrieveUpdateDestroyMovieView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
