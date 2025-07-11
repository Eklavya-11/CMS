from django.shortcuts import render
from .models import InventoryItem

def inventory_report(request):
    low_stock_items = InventoryItem.objects.filter(is_low_stock=True)
    return render(request, 'inventory/inventory_report.html', {'low_stock_items': low_stock_items})