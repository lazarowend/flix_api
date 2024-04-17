from django.urls import path
from . views import CreateListMovie, DetailUpdateDeleteMovie


urlpatterns = [
   path('movies/', CreateListMovie.as_view(), name='create_list_genre'),
   path('movies/<int:pk>/', DetailUpdateDeleteMovie.as_view(), name='detail_update_delete_genre'),
]
