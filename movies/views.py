from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializers import MovieModelSerializer


class CreateListMovie(APIView):

    def get(self, request):
        queryset = Movie.objects.all()

        serializer = MovieModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        title = request.data['title']
        
        movie = Movie.objects.filter(title=title)
        if movie.exists():
            return Response('Movie already exists', status=status.HTTP_200_OK)

        serializer = MovieModelSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DetailUpdateDeleteMovie(APIView):

    
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return None


    def get(self, request, pk):
        movie = self.get_object(pk)

        if movie is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MovieModelSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        movie = self.get_object(pk)

        if movie is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MovieModelSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_object(pk)

        if movie is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        Movie.delete(movie)
        return Response(status=status.HTTP_204_NO_CONTENT)