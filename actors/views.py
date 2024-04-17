from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from actors.models import Actor
from actors.serializers import ActorModelSerializer


class CreateListActor(APIView):

    def get(self, request):
        queryset = Actor.objects.all()
        serializer = ActorModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        name = request.data['name']

        actor = Actor.objects.filter(name=name)
        if actor.exists():
            return Response('Actor already exists', status=status.HTTP_200_OK)
        
        serializer = ActorModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        

class DetailUpdateDeleteActor(APIView):

    def get_object(self, pk):
        try:
            return Actor.objects.get(pk=pk)
        except Actor.DoesNotExist:
            return None


    def get(self, request, pk):
        actor = self.get_object(pk)

        if actor is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ActorModelSerializer(actor)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        actor = self.get_object(pk)
        
        if actor is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ActorModelSerializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        actor = self.get_object(pk)

        if actor is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        Actor.delete(actor)
        return Response(status=status.HTTP_204_NO_CONTENT)