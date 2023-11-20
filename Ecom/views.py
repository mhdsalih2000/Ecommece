from django.shortcuts import render,redirect
from django.views.generic import DetailView
from .models import Catogory,Product,CartItem
from django.views import View
from account.models import CustomUser
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    Catogorys=Catogory.objects.all()
    context ={
        'Catogorys' : Catogorys
    }
    return render(request,'index.html',context)



def Shop(request):
    Products =  Product.objects.all()
    context ={
        'Products' : Products
    }
    return render(request,'shop.html',context)



def category_products(request, category_id):
    category = get_object_or_404(Catogory, pk=category_id)
    Products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'Products': Products,
    }
    return render(request, 'shop.html', context)




def Detail_view(request, pk):
    products =Product.objects.get(pk=pk)
    context = {
        'products': products,   
    }
    return render(request, 'detail.html', context)






    

def Add_to_cart(request,pk):

    if request.user.is_authenticated:
        product = Product.objects.get(pk=pk)
        user = request.user
        cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
        if not created:
          cart_item.quantity += 1
          cart_item.save()
        return redirect('Ecom:cart_view')
    return redirect('account:login')
    



def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})



def remove_item_from_cart(request, id):
    cart_item = get_object_or_404(CartItem, id=id, user=request.user)
    cart_item.delete()
    return redirect('Ecom:cart_view')  


def decrease_item_quantity(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        remove_item_from_cart(request,pk)
    return redirect('Ecom:cart_view')





