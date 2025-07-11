from django.shortcuts import render
from django.http import JsonResponse
from .models import MenuItem

def menu_list(request):
    menu_items = MenuItem.objects.filter(is_available=True)
    return render(request, 'menu/menu_list.html', {'menu_items': menu_items})

def add_to_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        
        try:
            item = MenuItem.objects.get(id=item_id)
        except MenuItem.DoesNotExist:
            return JsonResponse({'error': 'Item not found'}, status=404)
        
        # Add the item to the cart in the session
        cart = request.session.get('cart', [])
        cart.append(item_id)  # Add item to cart (you may choose to increment quantity if the item already exists)
        request.session['cart'] = cart  # Save to session

        return JsonResponse({'message': f'Item "{item.name}" added to cart successfully!'})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
    
# View for placing the order
def place_order(request):
    if request.method == 'POST':
        # Get the selected items from the POST request (checkboxes)
        selected_items = request.POST.getlist('items')

        # Here, you can implement order creation logic based on selected items

        # Clear the cart after placing the order
        request.session['cart'] = []

        return redirect('order_success')  # Redirect to a success page after placing the order

    else:
        # Display cart items on the Place Order page
        cart_items = request.session.get('cart', [])
        menu_items = MenuItem.objects.filter(id__in=[item['id'] for item in cart_items])

        return render(request, 'orders/place_order.html', {'menu_items': menu_items})

# def menu_list(request):
#     query = request.GET.get('search', '')  # Get search query from URL params
#     if query:
#         menu_items = MenuItem.objects.filter(name__icontains=query)  # Filter items by name (case insensitive)
#     else:
#         menu_items = MenuItem.objects.all()  # If no search query, show all menu items
    
#     return render(request, 'menu/menu_list.html', {'menu_items': menu_items, 'search_query': query})