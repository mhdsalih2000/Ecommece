from django.urls import path,include,re_path
from . import views

app_name ='Checkout'

urlpatterns = [
    path('checkout/',views.checkout,name='checkout'),

]