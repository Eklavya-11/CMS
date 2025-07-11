from django import forms
from .models import OrderItem

class CartItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']  # We only need to handle the quantity

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget = forms.NumberInput(attrs={'min': 1, 'max': 10})  # Set min and max limits
