from rest_framework import routers, serializers, viewsets
from .models import PizzaOrder


class PizzaOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaOrder
        fields = ('id', 'name', 'flavours', 'number', 'size', 'customer_name', 'customer_address', 'ordered_time', 'status',)
        # excludes = ('status',)
        # exclude = ('status',)
        # read_only_fields = ('status', 'ordered_time',)
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': False},
            'flavours': {'read_only': False},
            'number': {'read_only': False},
            'size': {'read_only': False},
            'customer_name': {'read_only': False},
            'customer_address': {'read_only': False},
            'ordered_time': {'read_only': True},
            'status': {'read_only': True}
        }


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaOrder
        fields = ('id', 'name', 'flavours', 'number', 'size', 'customer_name', 'customer_address', 'ordered_time', 'status',)
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': True},
            'flavours': {'read_only': True},
            'number': {'read_only': True},
            'size': {'read_only': True},
            'customer_name': {'read_only': True},
            'customer_address': {'read_only': True},
            'ordered_time': {'read_only': True},
            'status': {'read_only': False}
        }

