from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import routers
from order_app import views
from .models import PizzaOrder
from .serializers import PizzaOrderSerializer

router = routers.DefaultRouter()
router.register(r'customer_orders', views.CustomerViewSet, base_name='pizzaorder')


class ListAllTests(APITestCase, URLPatternsTestCase):

    urlpatterns = [
        path('', include(router.urls)),
    ]
    url = '/customer_orders/'

    def test_list(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
