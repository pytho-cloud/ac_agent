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
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import AC
from .serializers import ACSerializer
from .filters import ACFilter
from rest_framework.generics import ListAPIView

class ACListAPIView(ListAPIView):
    serializer_class = ACSerializer

    def get_queryset(self):
        qs = AC.objects.filter(is_available=True)

        brand = self.request.query_params.get("brand")
        model = self.request.query_params.get("model_name")
        condition = self.request.query_params.get("condition")
        ac_type = self.request.query_params.get("ac_type")

        if brand:
            qs = qs.filter(brand=brand)
        if model:
            qs = qs.filter(model_name=model)
        if condition:
            qs = qs.filter(condition=condition)
        if ac_type:
            qs = qs.filter(ac_type=ac_type)

        return qs




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
    



class ACView(APIView):

    def get(self, request):

        brands = AC.objects.values_list("brand", flat=True).distinct()
        models = AC.objects.values_list("model_name", flat=True).distinct()
        conditions = AC.objects.values_list("condition", flat=True).distinct()
        ac_types = AC.objects.values_list("ac_type", flat=True).distinct()

        return Response({
            "brand": list(brands),
            "model_name": list(models),
            "condition": list(conditions),
            "ac_type": list(ac_types),
        })



        

