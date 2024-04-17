from rest_framework.views import APIView
from rest_framework.response import Response
from reviews.models import Review
from rest_framework import status
from reviews.serializers import ReviewModelSerializer


class CreateListReview(APIView):

    def get(self, request):
        queryset = Review.objects.all()

        serializer = ReviewModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReviewModelSerializer(data=request.data)

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

        serializer = ReviewModelSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        review = self.get_object(pk)

        if review is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewModelSerializer(review, data=request.data)
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
            