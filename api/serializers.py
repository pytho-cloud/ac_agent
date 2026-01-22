# serializers.py
from rest_framework import serializers
from .models import *

class ACImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ACImage
        fields = ['image']

class ACSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)  # <- this makes DRF return full URL

    class Meta:
        model = AC
        fields = "__all__"

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class BookServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookService
        fields = "__all__"


class ProductSellSerializer(serializers.ModelSerializer):

    class Meta :
        model = ProductSell
        fields = '__all__'


class ProductSellImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSellImages
        fields = "__all__"

class MaintainenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintainence
        fields = "__all__"
        
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"