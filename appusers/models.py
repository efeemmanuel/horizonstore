
from django.db import models


#import django default user
from django.contrib.auth.models import User


# Create your models here.

        
       




class Products(models.Model):
    ALL_DEPARTMENT = [
    ("fruits", "fruits"),
    ("vegetables", "vegetables"),
    ("meats", "meats"),
    ("fast foods", "fast foods"),
    ("drinks", "drinks"),
    ]
    ALL_PRODUCT_TYPE = [
    ("featured products", "featured products"),
    ("latest products", "latest products"),
    ("top reated products", "top reated products"),
    ("review products", "review products"),
    ("sales off", "sales off"),
    ]
    id = models.PositiveIntegerField(primary_key=True)
    item_photo = models.ImageField(upload_to='products')
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    department = models.CharField(blank=True, max_length=10, choices=ALL_DEPARTMENT)
    producttype = models.CharField(blank=True, max_length=30, choices=ALL_PRODUCT_TYPE)
    shipping = models.CharField(blank=True, max_length=20)
    avaliabilty = models.CharField(blank=True, max_length=20)
    weight = models.CharField(blank=True, max_length=20)
    description = models.TextField(blank=True, max_length=200)
    information = models.TextField(blank=True, max_length=200)
    reviews = models.TextField(blank=True, max_length=200)
    discount = models.CharField(blank=True, max_length=20)
    old_price = models.CharField(blank=True, max_length=20)
    
    def __str__(self):
        return f" {self.name} {self.item_photo} {self.price} {self.department} {self.producttype} {self.shipping} {self.avaliabilty} {self.weight} {self.description} {self.information}  {self.reviews} {self.discount} {self.old_price}"
 
 



# #    coupon models

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    expiration_date = models.DateField() 
 
 
 
 
 
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    
    def __str__(self):
        return str(self.id)
        
    def calculate_total_price(self):
        # Define your logic to calculate the total price based on the cart items
        total_price = sum(item.price for item in self.cartitems.all())
        return total_price

    @property
    def total_price(self):
        return self.calculate_total_price()

    @property
    def num_of_items(self):
        return sum(item.quantity for item in self.cartitems.all())



        
 
#  #refers to item in a cart
class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='items', default=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems', default=True)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.product.name
       
    @property   
    def price(self):
        return self.product.price * self.quantity
        




















class ShippingDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, default=True)
    lastname = models.CharField(max_length=100, default=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50, default=True)
    phone_number = models.CharField(max_length=50, default=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_details = models.ForeignKey(ShippingDetails, on_delete=models.CASCADE, default=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders', default=True)
    #cartitem = models.ForeignKey(CartItem, on_delete=models.CASCADE, related_name='items', default=True)
    date_created = models.DateTimeField(auto_now_add=True)  # Automatically set the date and time of creation

    def __str__(self):
        return f"Order {self.id}"


































#            checkout models here
# class ShippingDetails(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     address = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     country = models.CharField(max_length=50)






# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     shipping_details = models.ForeignKey(ShippingDetails, on_delete=models.CASCADE, default=True)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders', default=True)
#     #cartitem = models.ForeignKey(CartItem, on_delete=models.CASCADE, related_name='items', default=True)
#     date_created = models.DateTimeField(auto_now_add=True)  # Automatically set the date and time of creation
    









# class blog_post(models.Model):
#     photo = models.ImageField(upload_to='blog')
#     date =  models.DateField(null=True)
#     title = models.CharField(max_length=200)
#     description = models.CharField(max_length=200)
#     text = models.TextField(max_length=800)
#     author_pic = models.ImageField(upload_to='blog')
#     author = models.CharField(max_length=20)
#     categories = models.CharField(max_length=20)
#     tags = models.CharField(max_length=20)
    



