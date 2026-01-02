# serializers.py
from rest_framework import serializers
from .models import AC

class ACSerializer(serializers.ModelSerializer):
    class Meta:
        model = AC
        fields = "__all__"
