from django.urls import path
from . views import CreateListActor, DetailUpdateDeleteActor


urlpatterns = [
   path('actors/', CreateListActor.as_view(), name='create_list_actor'),
   path('actors/<int:pk>/', DetailUpdateDeleteActor.as_view(), name='detail_update_delete_actor'),
]

