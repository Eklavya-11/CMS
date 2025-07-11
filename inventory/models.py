from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    reorder_level = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def is_low_stock(self):
        return self.quantity <= self.reorder_level