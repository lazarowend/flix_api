from django.urls import path
from . views import ListCreateGenreView, RetrieveUpdateDestroyGenreView


urlpatterns = [
    path('genres/', ListCreateGenreView.as_view(), name='list_create_genre_view'),
    path('genres/<int:pk>/', RetrieveUpdateDestroyGenreView.as_view(), name='retrieve_update_destroy_genre_view'),
]
