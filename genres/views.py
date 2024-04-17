from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from genres.models import Genre
from genres.serializers import GenreModelSerializer


class CreateListGenre(APIView):
    
    def get(self, request):
        queryset = Genre.objects.all()
        serializer = GenreModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        name = request.data['name']
        
        genre = Genre.objects.filter(name=name)
        if genre.exists():
            return Response('Genre already exists', status=status.HTTP_200_OK)

        serializer = GenreModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailUpdateDeleteGenre(APIView):
    
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return None

    def get(self, request, pk):
        genre = self.get_object(pk)
        
        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GenreModelSerializer(genre)
        return Response(serializer.data)

    def put(self, request, pk):
        genre = self.get_object(pk)

        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GenreModelSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        genre = self.get_object(pk)

        if genre is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        Genre.delete(genre)
        return Response(status=status.HTTP_204_NO_CONTENT)
