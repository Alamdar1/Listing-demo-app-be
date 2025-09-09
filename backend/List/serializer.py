from rest_framework import serializers
from .models import List

class ListSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True, max_length=100)
    price = serializers.FloatField(required=True, error_messages={
            'required': 'Price is required',
            'invalid': 'Price must be a number'
        })
    class Meta:
        model = List
        fields = '__all__'