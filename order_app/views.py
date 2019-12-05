from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import PizzaOrder
from .serializers import PizzaOrderSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status


class CustomerViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_class = PizzaOrderSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('name', 'status', 'customer_name')

    def get_queryset(self):
        queryset = PizzaOrder.objects.all()
        return queryset

    def retrieve(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        obj = self.get_object()
        serializer = PizzaOrderSerializer(obj)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        order = PizzaOrder.objects.create(
            name=data['name'], flavours=data['flavours'],
            quantity=data['quantity'], size=data['size'],
            customer_name=data['customer_name'],
            customer_address=data['customer_address']
        )
        order.save()
        serializer = PizzaOrderSerializer(order)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        order = self.get_object()
        if order.status != 'Delivered':
            order.flavours = request.data.get('flavours', order.flavours)
            order.quantity = request.data.get('quantity', order.quantity)
            order.size = request.data.get('size', order.size)
        else:
            return Response({"OOPS !": "Its already delivered. Sorry, you can't change it now"})

        order.save()
        serializer = PizzaOrderSerializer(order, partial=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        if order.status == 'Open':
            order.delete()
            return Response('Order Deleted !')
        else:
            return Response('OOPS! : Order already in progress')

