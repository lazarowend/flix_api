from django.urls import path
from . views import CreateListGenre, DetailUpdateDeleteGenre


urlpatterns = [
   path('genres/', CreateListGenre.as_view(), name='create_list_genre'),
   path('genres/<int:pk>/', DetailUpdateDeleteGenre.as_view(), name='detail_update_delete_genre'),
]

