# Create views here.
from django.shortcuts import render
from orders.models import Order
from .models import Bill

def generate_bill(request, order_id):
    order = Order.objects.get(id=order_id)
    bill, created = Bill.objects.get_or_create(order=order, defaults={'total_amount': order.total_price()})
    return render(request, 'bill.html', {'bill': bill})