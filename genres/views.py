from genres.models import Genre
from genres.serializers import GenreModelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app.permissions import GlobalDefaultPermission


class ListCreateGenreView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer


class RetrieveUpdateDestroyGenreView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer
