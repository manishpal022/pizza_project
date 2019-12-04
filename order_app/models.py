from django.db import models
from django.utils import timezone


FLAVOURS_CHOICE = (
    ('MARGARITA', 'Margarita'),
    ('MARINARA', 'Marinara'),
    ('SALAMI', 'Salami'),
)

SIZE_CHOICE = (
    ('SMALL', 'Small'),
    ('MEDIUM', 'Medium'),
    ('LARGE', 'Large'),
)

STATUS_CHOICE = (
    ('OPEN', 'Open'),
    ('ACCEPTED', 'Accepted'),
    ('PREPARING', 'Preparing'),
    ('OUT FOR DELIVERY', 'Out for Delivery'),
    ('Delivered', 'Delivered'),
)


class PizzaOrder(models.Model):
    name = models.CharField(max_length=120, blank=False)
    flavours = models.CharField(max_length=20, choices=FLAVOURS_CHOICE)
    number = models.IntegerField(default=1)
    size = models.CharField(max_length=10, choices=SIZE_CHOICE, default='MEDIUM')
    customer_name = models.CharField(max_length=120, blank=False)
    customer_address = models.TextField(blank=False)
    ordered_time = models.DateTimeField(default=timezone.now, editable=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='OPEN')

    def __str__(self):
        return self.name
