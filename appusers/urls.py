
from django.urls import path, include
from .views import *
app_name="appusers"



urlpatterns = [
    
    path('',index,name='index' ),
    path('signup', Signup ,name='signup_page' ),
    path('fruitspage', Fruits ,name='fruits_page' ),
    path('vegetablespage', Vegetables,name='vegetables_page' ),
    path('meatpage', Meat,name='meat_page' ),
    path('fastfoodpage', Fast_food,name='fastfood_page' ),
    path('drinkspage', Drinks,name='drinks_page' ),
    path('allproduct', Allproduct,name='allproduct_page' ),
    path('shopdetails<int:id>', Shopdetails,name='shopdetails_page' ),
    path('search', search_feature,name='search-view' ),
    # path('blogdetails<int:id>', Blogdetails,name='blogdetails_page' ),

    path('add_to_cart', add_to_cart,name='add' ),
    path('remove_from_cart', remove_from_cart, name='remove_from_cart'),
    path('reduce_quantity', reduce_quantity, name='reduce_quantity'),
    path('increase_quantity', increase_quantity, name='increase_quantity'),
    path('cart', cart, name='cart'),
    path('cart', cart, name='cart_page'),
    # path("confirm_payment/<str:pk>", confirm_payment, name="add"),
    path('apply_coupon', apply_coupon, name='apply_coupon'),

    #urls for place-order/
    path('checkout', checkout, name='checkout'),
    path('pay', pay, name='pay'),

    #path('paypal', include('paypal.standard.ipn.urls')),
    #path('checkout', CheckoutView, name='checkout'),

]