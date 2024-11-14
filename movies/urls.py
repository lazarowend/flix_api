from django.urls import path
from . views import ListCreateMovieView, RetrieveUpdateDestroyMovieView


urlpatterns = [
   path('movies/', ListCreateMovieView.as_view(), name='create_list_movie'),
   path('movies/<int:pk>/', RetrieveUpdateDestroyMovieView.as_view(), name='detail_update_delete_movie'),
]
