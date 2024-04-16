from django.urls import path
from actors.views import CreateListActor, DetailUpdateDeleteActor


urlpatterns = [
   path('', CreateListActor.as_view(), name='create_list_actor'),
   path('<int:pk>/', DetailUpdateDeleteActor.as_view(), name='detail_update_delete_actor'),
]

