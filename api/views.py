from django.shortcuts import render 
from rest_framework import generics
from .models import AC
from .serializers import ACSerializer
from .filters import ACFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Review
from .serializers import ReviewSerializer
from rest_framework import viewsets


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