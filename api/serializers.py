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