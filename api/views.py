from django.shortcuts import render 
from rest_framework import generics
from .filters import ACFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Review
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import AC
from .filters import ACFilter
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from .models import *
from .serializers import *
from .serializers import ReviewsSerializer


class ACListAPIView(APIView):
    def get(self, request):
        new_ac = AC.objects.filter(is_available=True, is_home_active=True, condition="new")
        refurbish_ac = AC.objects.filter(is_available=True, is_home_active=True, condition="refurbished")

        new_serializer = ACSerializer(new_ac, many=True, context={'request': request})
        refurbish_serializer = ACSerializer(refurbish_ac, many=True, context={'request': request})

        return Response({
            "data_new": new_serializer.data,
            "data_refurbish": refurbish_serializer.data
        })


class ProductACAPIView(APIView):

    def get(self, request):

        data = AC.objects.filter(is_available=True)

        brand = request.GET.get("brand")
        model_name = request.GET.get("model_name")
        condition = request.GET.get("condition")
        ac_type = request.GET.get("ac_type")

        if brand:
            data = data.filter(brand=brand)

        if model_name:
            data = data.filter(model_name=model_name)

        if condition:
            data = data.filter(condition=condition)

        if ac_type:
            data = data.filter(ac_types=ac_type)

        serializer = ACSerializer(data, many=True)

        return Response(serializer.data)


# class ReviewViewSet(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     # filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['product_name', 'star']




class MaintenanceAPIView(APIView):
    def get(self, request):
        services = Maintainence.objects.filter(is_active=True)
        serializer = MaintainenceSerializer(services, many=True)
        return Response({
            "data": serializer.data,
            "status": 200
        }, status=status.HTTP_200_OK)

class ReviewsAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    # GET all active reviews
    def get(self, request):
        try:
            response = list(
                Reviews.objects.filter(is_active=True).values()
            )

            return Response(
                {"data": response, "status": 200},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    # POST new review
    def post(self, request):
        try:
            serializer = ReviewsSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save(is_active=False)  # admin approval system

                return Response(
                    {
                        "message": "Review submitted successfully. Waiting for approval.",
                        "data": serializer.data,
                        "status": 201
                    },
                    status=status.HTTP_201_CREATED
                )

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

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
            return Response({"message": "Contact form submitted successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class ACView(APIView):

    def get(self, request):

        brands = AC.objects.values_list("brand", flat=True).distinct()
        models = AC.objects.values_list("model_name", flat=True).distinct()
        conditions = AC.objects.values_list("condition", flat=True).distinct()
        ac_types = AC.objects.values_list("ac_types", flat=True).distinct()

        return Response({
            "brand": list(brands),
            "model_name": list(models),
            "condition": list(conditions),
            "ac_type": list(ac_types),
        })



        

class BookServiceView(APIView):

    def post(self, request):
        serializer = BookServiceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Saved"}, status=201)

        return Response(serializer.errors, status=400)



class ProductSellCreateAPIView(APIView):

    def post(self, request):
        serializer = ProductSellSerializer(data=request.data)

        if serializer.is_valid():
            product = serializer.save()

            images = request.FILES.getlist('images')
            for img in images:
                ProductSellImages.objects.create(
                    product=product,
                    images=img
                )

            return Response({
                "message": "Product with images uploaded successfully"
            }, status=201)

        return Response(serializer.errors, status=400)
