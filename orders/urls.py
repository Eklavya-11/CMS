from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('order_confirm/', views.order_confirm, name='order_confirm'),
]

# Note:
# Workaround 3 (Model Forms) – This will involve a more significant refactor of your application structure to accommodate form-based cart management.
# oof ek, the current django allows only custom filters to be passed + no built-in for quanity argument. Long term use: model forms
# line causing the workaround (removed):                 <!-- <input type="number" name="quantities[{{ cart_item.id }}]" value="{{ item_quantities|get_item_quantity:cart_item.id }}" min="1" max="10"> -->

# update: decided to use model forms in orders/forms.py - created new forms.py file