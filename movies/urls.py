from django.urls import path
from . views import ListCreateMovieView, RetrieveUpdateDestroyMovieView, MovieStatsView


urlpatterns = [
   path('movies/', ListCreateMovieView.as_view(), name='list_create_movie_view'),
   path('movies/<int:pk>/', RetrieveUpdateDestroyMovieView.as_view(), name='retrieve_update_destroy_movies_view'),
   path('movies/stats/', MovieStatsView.as_view(), name='movie_stats_view'),
]
