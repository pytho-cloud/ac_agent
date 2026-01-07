from django.shortcuts import render 
from rest_framework import generics
from .models import *
from .serializers import *
from .filters import ACFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Review
from .serializers import ReviewSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ACListAPIView(generics.ListAPIView):
    queryset = AC.objects.filter(is_available=True)  # ✅ use is_available
    serializer_class = ACSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ACFilter
    search_fields = ['brand', 'model_name']
    ordering_fields = ['price', 'energy_rating']



class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_name', 'star']





class MaintenanceAPIView(APIView):
    def get(self, request):
        try:
            response = list(Maintainence.objects.filter(is_active = True).values())
            print(response)
            return Response(
                {"data": response, "status": 200},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ReviewsAPIView(APIView):
    def get(self, request):
        try:
            print()
            response = list(Reviews.objects.filter(is_active = True).values())
            print(response,"sssssssssss")
            return Response(
                {"data": response, "status": 200},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            print(e)
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ContactAPIView(APIView):

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Contact form submitted successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)