from django.urls import path
from genres.views import CreateListGenre, DetailUpdateDeleteGenre


urlpatterns = [
   path('', CreateListGenre.as_view(), name='create_list_genre'),
   path('<int:pk>/', DetailUpdateDeleteGenre.as_view(), name='detail_update_delete_genre'),
]

