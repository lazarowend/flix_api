from reviews.models import Review
from reviews.serializers import ReviewModelSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from app.permissions import GlobalDefaultPermission


class ListCreateReviewView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer


class RetrieveUpdateDestroyReviewView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer
