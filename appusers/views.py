from django.shortcuts import render, redirect , get_object_or_404
app_name="appusers"
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .forms import Signupform
#from .forms import ShippingAddressForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator

from datetime import date
from decimal import Decimal

from .forms import CouponForm


from .forms import ShippingDetailsForm

from django.contrib import messages






# Create your views here.




def index(request):
    featured = Products.objects.filter(producttype="featured products")
    latest = Products.objects.filter(producttype="latest products")
    rated = Products.objects.filter(producttype="top reated products")
    review = Products.objects.filter(producttype="review products")
    # blogpost = blog_post.objects.all()
    
   
    if request.user.is_authenticated:
        global cart
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    
    
    data={
    'featured':featured, 'latest':latest, 'rated':rated, 'review':review, 'cart':cart,
    }
    return render(request, 'index.html',data)
    
    
def Fruits(request):
    latest = Products.objects.filter(producttype="latest products")
    products = Products.objects.filter(department="fruits")
    paginator = Paginator(products, 4)  # Display 10 items per page
    page_number = request.GET.get('fruits')  # Assuming the URL parameter is 'page'
    page_obj = paginator.get_page(page_number)
    
    if request.user.is_authenticated:
        global cart
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    
    data={
    'latest':latest, 'products':products, 'cart':cart, 'page_obj':page_obj
    }
    return render(request, 'fruitspage.html', data)
    
def Vegetables(request):
    latest = Products.objects.filter(producttype="latest products")
    products = Products.objects.filter(department="vegetables")
    paginator = Paginator(products, 4)  # Display 10 items per page
    page_number = request.GET.get('vegetables')  # Assuming the URL parameter is 'page'
    page_obj = paginator.get_page(page_number)
    
    if request.user.is_authenticated:
        global cart
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        
    
    data={
    'latest':latest, 'products':products, 'cart':cart, 'page_obj':page_obj
    }
    return render(request, 'vegetablespage.html', data)
    
def Meat(request):
    latest = Products.objects.filter(producttype="latest products")
    products = Products.objects.filter(department="meats")
    paginator = Paginator(products, 4)  # Display 10 items per page
    page_number = request.GET.get('meat')  # Assuming the URL parameter is 'page'
    page_obj = paginator.get_page(page_number)
    
    
    if request.user.is_authenticated:
        global cart
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    
    data={
    'latest':latest, 'products':products, 'cart':cart, 'page_obj':page_obj
    }
    return render(request, 'meatpage.html', data)
    
    
    
def Fast_food(request):
    latest = Products.objects.filter(producttype="latest products")
    products = Products.objects.filter(department="fast foods")
    paginator = Paginator(products, 4)  # Display 10 items per page
    page_number = request.GET.get('fastfood')  # Assuming the URL parameter is 'page'
    page_obj = paginator.get_page(page_number)
    
    
    if request.user.is_authenticated:
        global cart
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    
    data={
    'latest':latest, 'products':products, 'cart':cart, 'page_obj':page_obj
    }
    return render(request, 'fastfoodpage.html', data)
    
    
    
def Drinks(request):
    latest = Products.objects.filter(producttype="latest products")
    products = Products.objects.filter(department="drinks")
    paginator = Paginator(products, 4)  # Display 10 items per page
    page_number = request.GET.get('fastfood')  # Assuming the URL parameter is 'page'
    page_obj = paginator.get_page(page_number)
    if request.user.is_authenticated:
        global cart
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    
    data={
    'latest':latest, 'products':products, 'cart':cart, 'page_obj':page_obj
    }
    return render(request, 'drinkspage.html', data)
    




def Signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "account created sucessfully")
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/login')
    else:
        form = Signupform()
    return render(request,"registration/signup.html", {'form': form})
    
    
def search_feature(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter your model by the search query
        #posts = Products.objects.filter(name__contains=search_query)
        posts = Products.objects.filter(Q(name__icontains=search_query) | Q(department__icontains=search_query))
        return render(request, 'search.html', {'query':search_query, 'posts':posts})
    else:
        return render(request, 'search.html',{})
        

# def Blogdetails(request, id):
#     detail = blog_post.objects.get(id=id)
#     data = {'detail':detail,}
#     return render(request, 'blogdetails.html', data)



def Allproduct(request):
    latest = Products.objects.filter(producttype="latest products")
    sales = Products.objects.filter(producttype="sales off")
    products = Products.objects.all()
    paginator = Paginator(products, 8)  # Display 10 items per page
    page_number = request.GET.get('allproduct')  # Assuming the URL parameter is 'page'
    page_obj = paginator.get_page(page_number)

    if request.user.is_authenticated:
        global cart
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)

    data={
    'latest':latest, 'products':products,'sales':sales, 'cart':cart, 'page_obj':page_obj
    }
    return render(request, 'allproduct.html', data)
    


def Shopdetails(request, id):
    details = Products.objects.get(id=id)

    if request.user.is_authenticated:
        global cart
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    
    data = {'details':details, 'cart':cart,}
    return render(request, 'shopdetails.html', data)   
    
    
  

    
    
def add_to_cart(request):
    data = json.loads(request.body)
    x_id = data["id"]

    #any issue,change product to x
    product = Products.objects.get(id=x_id)
    
    if request.user.is_authenticated:
            global cart
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
            cartitem, created =CartItem.objects.get_or_create(cart=cart, product=product)
            cartitem.quantity += 1
            cartitem.save()
            
            num_of_item = cart.num_of_items
            print(cartitem)
    
    return JsonResponse(num_of_item, safe=False)
    


def remove_from_cart(request):
    data = json.loads(request.body)
    cart_item_id = data["id"]

    if request.user.is_authenticated:
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            cart_item.delete()

            cart = Cart.objects.get(user=request.user, completed=False)
            num_of_items = cart.num_of_items

            return JsonResponse(num_of_items, safe=False)
        except CartItem.DoesNotExist:
            # Handle case when the cart item does not exist
            pass

    return JsonResponse({}, status=400)










def reduce_quantity(request):
    data = json.loads(request.body)
    cart_item_id = data["id"]

    if request.user.is_authenticated:
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()

            return JsonResponse({"quantity": cart_item.quantity}, safe=False)
        except CartItem.DoesNotExist:
            # Handle case when the cart item does not exist
            pass

    return JsonResponse({}, status=400)


def increase_quantity(request):
    data = json.loads(request.body)
    cart_item_id = data["id"]

    if request.user.is_authenticated:
        try:
            cart_item = CartItem.objects.get(id=cart_item_id)
            cart_item.quantity += 1
            cart_item.save()

            return JsonResponse({"quantity": cart_item.quantity}, safe=False)
        except CartItem.DoesNotExist:
            # Handle case when the cart item does not exist
            pass

    return JsonResponse({}, status=400)



#    this is the main cououn views
# def apply_coupon(request):
#     error_message = ''  # Initialize the variable with an empty string
#     if request.method == 'POST':
#         code = request.POST.get('code')
#         try:
#             coupon = Coupon.objects.get(code=code, active=True, valid_from__lte=date.today(), valid_to__gte=date.today())
#             # Apply coupon logic here
#             return redirect('/success')
#         except Coupon.DoesNotExist:
#             error_message = 'Invalid coupon code'
#     return render(request, 'apply.html', {'error_message': error_message})

# def success(request):
#     return render(request, 'success.html')




def cart(request):
    global cart
    cart = None
    cartitems = []
    if request.user.is_authenticated:
        
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()
    
    data = {"cart":cart, "items":cartitems, "show_checkout": bool(cartitems)}
    return render(request, "cart.html", data)






# my main cart views
# def cart(request):

#     cart = None 
#     cartitems = []  # Replace with your own logic to fetch cart data
#     coupon_form = ApplyCouponForm()

#     if request.user.is_authenticated:
#             cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
#             cartitems = cart.cartitems.all()

#     if request.method == 'POST':
#         coupon_form = ApplyCouponForm(request.POST)
#         if coupon_form.is_valid():
#             code = coupon_form.cleaned_data['code']
#             try:
#                 coupon = Coupon.objects.get(code=code, active=True, valid_from__lte=date.today(), valid_to__gte=date.today())
#                 # Apply coupon logic here
#                 discount = coupon.discount
#                 # Apply the discount to the cart total price
#                 cart.total_price -= cart.total_price * (discount / 100)
#                 cart.save()
#                 return redirect('/cart')  # Redirect back to the cart page after applying the coupon
#             except Coupon.DoesNotExist:
#                 coupon_form.add_error('code', 'Invalid coupon code')

#     context = {
#         'cart': cart,
#         'coupon_form': coupon_form,
#         'items':cartitems
#     }
#     return render(request, 'cart.html', context)



# just copied



# def cart(request):
#     cart = None
#     cartitems = []  # Replace with your own logic to fetch cart data
#     coupon_form = ApplyCouponForm()

#     if request.user.is_authenticated:
#         cart, create = Cart.objects.get_or_create(user=request.user, completed=False)
#         cartitems = cart.cartitems.all()

#     if request.method == 'POST':
#         coupon_form = ApplyCouponForm(request.POST)
#     if coupon_form.is_valid():
#         code = coupon_form.cleaned_data['code']
#         try:
#             coupon = Coupon.objects.get(code=code, active=True, valid_from__lte=date.today(), valid_to__gte=date.today())
#             # Apply coupon logic here
#             discount = Decimal(coupon.discount)  # Convert discount to Decimal
#             # Apply the discount to the cart total price
#             cart.total_price -= cart.total_price * (discount / Decimal(100))
#             cart.save()
#             return redirect('/cart')  # Redirect back to the cart page after applying the coupon
#         except Coupon.DoesNotExist:
#             coupon_form.add_error('code', 'Invalid coupon code')

#     context = {
#         'cart': cart,
#         'coupon_form': coupon_form,
#         'items': cartitems
#     }
#     return render(request, 'cart.html', context)






def apply_coupon(request):

    global cart
    cart = None
    cart_items = []

    if request.user.is_authenticated:
        
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cart_items = cart.cartitems.all()

    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code=code, expiration_date__gte=date.today())
                # Calculate the discounted price
                cart_items = CartItem.objects.filter(cart=cart)
                cart.discounted_price = sum(item.price for item in cart_items) - float(coupon.discount)
                cart.save()

                return redirect('/cart')
            except Coupon.DoesNotExist:
                # Handle invalid or expired coupon code
                # You can display an error message to the user or take appropriate action
                pass
    else:
        form = CouponForm()

    return render(request, 'cart.html', {"cart": cart, "items": cart_items, "coupon_form": form})







def checkout(request):

    if request.user.is_authenticated:
        global cart
        cart = Cart.objects.get(user=request.user, completed=False)
        cartitems = cart.cartitems.all()
    else:
        cart = None
        cartitems = []
    
    
    if request.method == 'POST':
        form = ShippingDetailsForm(request.POST)
        if form.is_valid():
            shipping_details = form.save(commit=False)
            shipping_details.user = request.user
            shipping_details.save()
            
            order = Order.objects.create(user=request.user, shipping_details=shipping_details)
            # Additional order processing logic if needed
            
            # Mark the cart as completed
            
            
            cart.completed = True
            cart.save()
            
            # Delete the cart items associated with the cart
            cart.cartitems.all().delete()
            
            
            return redirect('/pay')  # Redirect to the payment page
    else:
            form = ShippingDetailsForm(request.POST)
    
    context = {
        'form': form,
        'cart':cart,
        'items':cartitems
    }
    return render(request, 'checkout.html', context)



def pay(request):
    global cart
    cart = None
    cartitems = []
    if request.user.is_authenticated:
        
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()
        
    
    data = {"cart":cart, "items":cartitems}

    return render(request, 'pay.html', data)


# def confirm_payment(request, pk):
#     cart = Cart.objects.get(id=pk)
#     cart.completed = True
#     cart.save()
#     messages.success(request, "Payment made successfully")
#     return redirect('/index')


# def checkout(request):
#     cart = Cart.objects.get(user=request.user, completed=False)

#     if request.method == 'POST':
#         form = ShippingDetailsForm(request.POST)
#         if form.is_valid():
#             shipping_details = form.save(commit=False)
#             shipping_details.user = request.user
#             shipping_details.save()

#             order = Order.objects.create(user=request.user, shipping_details=shipping_details, cart=cart)
#             # Additional order processing logic if needed

#             # Mark the cart as completed after creating the order
#             cart.completed = True
#             cart.save()

#             return redirect('order-success')  # Redirect to a success page after creating the order
#     else:
#         form = ShippingDetailsForm()

#     context = {
#         'form': form,
#         'cart': cart
#     }
#     return render(request, 'checkout.html', context)













# def checkout(request):
#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
#         cartitems = cart.cartitems.all()
#     else:
#         cart = None
#         cartitems = []
#     data = {'cart':cart, 'items':cartitems}
#     return render(request, "checkout.html",data)










# def checkout(request):
#     if request.user.is_authenticated:
#         global cart
#         cart = Cart.objects.get(user=request.user, completed=False)
#         cartitems = cart.cartitems.all()
#     else:
#         cart = None
#         cartitems = []
    
    
#     if request.method == 'POST':
#         form = ShippingAddressForm(request.POST)
#         if form.is_valid():
#             address = form.cleaned_data.get('address')
#             # Process the form data, update the cart, etc.
#             # Redirect to the next step in the checkout process
#             return redirect('checkout:payment')
#     else:
#         form = ShippingAddressForm()
    
#     context = {
#         'form': form,
#         'cart': cart,
#         'items':cartitems
#     }
#     return render(request, 'checkout.html', context)


# view for place_order



































