from django.urls import path
from . views import CreateListReview, DetailUpdateDeleteReview


urlpatterns = [
   path('reviews/', CreateListReview.as_view(), name='create_list_review'),
   path('reviews/<int:pk>/', DetailUpdateDeleteReview.as_view(), name='detail_update_delete_review'),
]
