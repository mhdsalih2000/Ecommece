from django.urls import path,include,re_path
from . import views

app_name ='Ecom'

urlpatterns = [
    path('',views.home,name='home'),
    path('shop/',views.Shop,name='shop'),
    path('products/<int:category_id>', views.category_products, name='category_products'),
    path('detail/<int:pk>', views.Detail_view, name='Detail_view'),
    path('addtocart/<int:pk>',views.Add_to_cart,name='addtocart'),
    path('cart_view',views.view_cart,name='cart_view'),
    path('remove_cart_item/<int:id>',views.remove_item_from_cart,name='remove_cart_item'),
    path('remove_one_cart/<int:pk>',views.decrease_item_quantity,name='decrease_qty')
    
   
   


]