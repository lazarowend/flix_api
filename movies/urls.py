from django.urls import path
from . views import ListCreateMovieView, RetrieveUpdateDestroyMovieView


urlpatterns = [
   path('movies/', ListCreateMovieView.as_view(), name='list_create_movie_view'),
   path('movies/<int:pk>/', RetrieveUpdateDestroyMovieView.as_view(), name='retrieve_update_destroy_movies_view'),
]
