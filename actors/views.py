from actors.models import Actor
from actors.serializers import ActorModelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateActorView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer


class RetrieveUpdateDestroyActorView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer