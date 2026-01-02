from django.shortcuts import render 
from rest_framework import generics
from .models import AC
from .serializers import ACSerializer
from .filters import ACFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.
class ACListAPIView(generics.ListAPIView):
    queryset = AC.objects.filter(is_available=True)  # ✅ use is_available
    serializer_class = ACSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ACFilter
    search_fields = ['brand', 'model_name']
    ordering_fields = ['price', 'energy_rating']