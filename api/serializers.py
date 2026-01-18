# serializers.py
from rest_framework import serializers
from .models import *

class ACSerializer(serializers.ModelSerializer):
    class Meta:
        model = AC
        fields = "__all__"





class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'name',
            'product_name',
            'star',
            'phone_number',
            'email',
            'created_at',
        ]



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
