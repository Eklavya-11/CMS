
# Create models here.
from django.db import models
from orders.models import Order

class Bill(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    is_paid = models.BooleanField(default=False)