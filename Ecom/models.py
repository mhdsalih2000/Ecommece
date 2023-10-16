from django.db import models
from account.models import CustomUser
# Create your models here.
class Catogory(models.Model):
    Catogory_name        =models.CharField(max_length=100,unique=True,blank=False)
    Catogory_description =models.CharField(max_length=100,blank=True)
    Catogory_image       =models.ImageField(upload_to='static/img')

    def __str__ (self):
        return self.Catogory_name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Catogory, on_delete=models.CASCADE)
    slug =models.SlugField(null=True)
    Product_img =models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.name
    
    

class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)