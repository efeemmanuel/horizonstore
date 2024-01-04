from django.contrib import admin
from .models import  *
# Register your models here.





admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Coupon)
admin.site.register(ShippingDetails)




class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'shipping_address', 'discounted_price', 'get_ordered_products')

    def shipping_address(self, obj):
        return f"{obj.shipping_details.address}, {obj.shipping_details.city}, {obj.shipping_details.state}, {obj.shipping_details.country}"
    shipping_address.short_description = 'Shipping Address'


    #def calculate_total_price(self, obj):
        # Calculate the total price based on the cart items
        #cart = obj.cart.cartitems.all()
        #total_price = sum(item.price for item in self.cartitems.all())
        #return total_price
    #calculate_total_price.short_description = 'Total Price'

    def discounted_price(self, obj):
        return obj.cart.discounted_price
    discounted_price.short_description = 'Discounted Price'

    def get_ordered_products(self, obj):
        # Retrieve the related cart items for the order
        cart_items = obj.cart.cartitems.all()

        # Create a list of product names and quantities
        products = []
        for cart_item in cart_items:
            product = cart_item.product
            quantity = cart_item.quantity
            products.append(f"{product.name} (Quantity: {quantity})")

        # Join the product names with commas and return
        return ', '.join(products)
    get_ordered_products.short_description = 'Ordered Products'

admin.site.register(Order, OrderAdmin)