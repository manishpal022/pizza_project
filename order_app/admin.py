from django.contrib import admin
from .models import PizzaOrder


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'flavours', 'quantity', 'size', 'customer_name', 'status')
    list_display_links = ('id', 'name')
    list_editable = ('status',)
    list_filter = ('status',)
    list_per_page = 10
    search_fields = ('id', 'name', 'status')


admin.site.register(PizzaOrder, OrderAdmin)
