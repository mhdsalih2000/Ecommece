from django.shortcuts import render
from Ecom.models import CartItem

# Create your views here.

def checkout(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    if cart_items is not None:
        
        total_price = sum(item.product.price * item.quantity for item in cart_items)


    # In a real application, you would implement payment processing logic here.
    # For simplicity, let's assume a successful checkout clears the 

        cart_items.delete()
        return render(request, 'checkout.html', {'total_price': total_price})
    else:
        return render(request,'cart.html')

    

    
