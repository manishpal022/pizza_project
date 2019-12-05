from django.db import models
from datetime import datetime


FLAVOURS_CHOICE = (
    ('Margarita', 'Margarita'),
    ('Marinara', 'Marinara'),
    ('Salami', 'Salami'),
)

SIZE_CHOICE = (
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
)

STATUS_CHOICE = (
    ('Open', 'Open'),
    ('Accepted', 'Accepted'),
    ('Preparing', 'Preparing'),
    ('OnWay', 'OnWay'),
    ('Delivered', 'Delivered'),
)


class PizzaOrder(models.Model):
    name = models.CharField(max_length=50, blank=False)
    flavours = models.CharField(max_length=20, choices=FLAVOURS_CHOICE)
    quantity = models.IntegerField()
    size = models.CharField(max_length=10, choices=SIZE_CHOICE)
    customer_name = models.CharField(max_length=30, blank=False)
    customer_address = models.TextField(blank=False)
    ordered_time = models.DateTimeField(default=datetime.now, editable=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='Open')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-ordered_time']
        unique_together = ('name', 'flavours', 'quantity', 'size')

