from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import PizzaOrder
from .serializers import PizzaOrderSerializer, OwnerSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class PizzaOrderViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put', 'patch', 'post']
    # queryset = PizzaOrder.objects.all()
    serializer_class = PizzaOrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ('name', 'status')
    search_fields = ('customer_name',)
    ordering_filters = ('ordered_time',)
    ordering = ('-id',)

    def get_queryset(self):
        customer_name = self.request.query_params.get('customer_name', None)

        if customer_name:
            undelivered_queryset = PizzaOrder.objects.filter(customer_name__icontains=customer_name)
        else:
            undelivered_queryset = PizzaOrder.objects.all()

        return undelivered_queryset

    def list(self, request, *args, **kwargs):
        # orders = self.get_queryset()
        orders = self.get_queryset()
        serializer = PizzaOrderSerializer(orders, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        obj = self.get_object()
        serializer = PizzaOrderSerializer(obj)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        if not PizzaOrder.objects.filter(data['name']).filter(data['flavours']).filter(data['size']).exists():
            order = PizzaOrder.objects.create(
                name=data['name'], flavours=data['flavours'],
                number=data['number'], size=data['size'],
                customer_name=data['customer_name'],
                customer_address=data['customer_address']
            )
            order.save()
            serializer = PizzaOrderSerializer(order)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        import pdb;pdb.set_trace()
        order = self.get_object()
        data = request.data
        if order.status != 'Out for Delivery' or 'Delivered':
            order.flavours = data['flavours']
            order.number = data['number']
            order.size = data['size']

        order.save()
        serializer = PizzaOrderSerializer(order)
        return Response(serializer.data)

    # @action(Detail=False)
    # def repeat_last_order(self, request, **kwargs):


class OwnerViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'put', 'patch']
    serializer_class = OwnerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ('name', 'status')
    search_fields = ('customer_name',)
    ordering_filters = ('ordered_time',)
    ordering = ('-id',)

    def get_queryset(self):
        customer_name = self.request.query_params.get('customer_name', None)

        if customer_name:
            undelivered_queryset = PizzaOrder.objects.filter(customer_name__icontains=customer_name)
        else:
            undelivered_queryset = PizzaOrder.objects.all()

        return undelivered_queryset

    # def list(self, request, *args, **kwargs):
    #     # orders = self.get_queryset()
    #     orders = PizzaOrder.objects.all()
    #     serializer = OwnerSerializer(orders, many=True)
    #     return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace()
        order = self.get_object()
        data = request.data
        order.status = data['status']

        order.save()
        serializer = PizzaOrderSerializer(order)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        order = self.get_object()
        order.delete()

        return Response('Order Deleted !')
