from django.urls import path
from reviews.views import CreateListReview, DetailUpdateDelete


urlpatterns = [
   path('', CreateListReview.as_view(), name='create_list_review'),
   path('<int:pk>/', DetailUpdateDelete.as_view(), name='detail_update_delete_review'),
]

