from rest_framework import serializers
from .models import PizzaOrder
from rest_framework.validators import UniqueTogetherValidator


class PizzaOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaOrder
        fields = ('id', 'name', 'flavours', 'quantity', 'size', 'customer_name', 'customer_address', 'ordered_time', 'status')
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': False},
            'flavours': {'read_only': False},
            'quantity': {'read_only': False},
            'size': {'read_only': False},
            'customer_name': {'read_only': False},
            'customer_address': {'read_only': False},
            'ordered_time': {'read_only': True},
            'status': {'read_only': True}
        }

