from django.urls import path
from . views import ListCreateReviewView, RetrieveUpdateDestroyReviewView


urlpatterns = [
   path('reviews/', ListCreateReviewView.as_view(), name='list_create_review_view'),
   path('reviews/<int:pk>/', RetrieveUpdateDestroyReviewView.as_view(), name='retrieve_update_destroy_review_view'),
]
