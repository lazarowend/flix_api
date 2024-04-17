from rest_framework.views import APIView
from rest_framework.response import Response
from reviews.models import Review
from rest_framework import status
from reviews.serializers import ReviewSerializer


class CreateListReview(APIView):

    def get(self, request):
        queryset = Review.objects.all()

        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailUpdateDeleteReview(APIView):
    
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return None

    def get(self, resquest, pk):
        review = self.get_object(pk)

        if review is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        review = self.get_object(pk)

        if review is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        review = self.get_object(pk)

        if review is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        Review.delete(review)
        return Response(status=status.HTTP_204_NO_CONTENT)
            