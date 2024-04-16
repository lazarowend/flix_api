from django.urls import path
from movies.views import CreateListMovie, DetailUpdateDeleteMovie


urlpatterns = [
   path('', CreateListMovie.as_view(), name='create_list_genre'),
   path('<int:pk>/', DetailUpdateDeleteMovie.as_view(), name='detail_update_delete_genre'),
]
