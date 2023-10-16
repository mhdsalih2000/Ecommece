from django.contrib import admin
from .models import Catogory,Product,CartItem
# Register your models here.
admin.site.register(Catogory)
admin.site.register(Product)
admin.site.register(CartItem)