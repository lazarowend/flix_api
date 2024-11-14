from django.urls import path
from . views import ListCreateActorView, RetrieveUpdateDestroyActorView


urlpatterns = [
   path('actors/', ListCreateActorView.as_view(), name='list_create_actor_view'),
   path('actors/<int:pk>/', RetrieveUpdateDestroyActorView.as_view(), name='retrieve_update_destroy_actor_view'),
]

