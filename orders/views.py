from django.shortcuts import render, redirect
from menu.models import MenuItem
from .models import Order, OrderItem
from .forms import CartItemForm

def place_order(request):
    # Check if the user is logged in
    if not request.user.is_authenticated:
        return redirect('register') 

    if request.method == 'POST':
        selected_items = request.POST.getlist('items')
        item_quantities = request.POST.getlist('quantities')  # Get the quantities
        
        # Create the order for the logged-in user
        order = Order.objects.create(customer=request.user)
        
        # Create OrderItems for each selected menu item with the specified quantity
        for item_id, quantity in zip(selected_items, item_quantities):
            item = MenuItem.objects.get(id=item_id)
            OrderItem.objects.create(order=order, item=item, quantity=int(quantity))  # Save quantity as integer
        
        # Optionally clear the cart after the order is placed
        request.session['cart'] = []  # Reset cart after placing the order
        
        return redirect('order_confirm') 
    
    else:
        # If GET request, display cart items on the place order page
        cart_items = request.session.get('cart', [])  # Get cart from session
        menu_items = MenuItem.objects.filter(id__in=cart_items)  # Get menu items matching cart ids
        
        # Prepare a dictionary of menu items and their current quantities in the cart
        item_quantities = {item.id: cart_items.count(item.id) for item in menu_items}
        
        cart_forms = []
        for item in menu_items:
            # Create a form for each cart item with its quantity
            form = CartItemForm(initial={'quantity': item_quantities.get(item.id, 1)})
            cart_forms.append({'item': item, 'form': form})
        
        return render(request, 'orders/place_order.html', {
            'menu_items': menu_items,
            'item_quantities': item_quantities,
            'cart_forms': cart_forms
        })

def order_confirm(request):
    if not request.user.is_authenticated:
        return redirect('register')

    # if request.method == 'POST':
        # Process form data, save the order or address, etc.
        # street_address = request.POST.get('street-address')
        # city = request.POST.get('city')
        # state = request.POST.get('state')
        # zip_code = request.POST.get('zip')

        # return redirect('home')

    return render(request, 'orders/order_confirm.html')