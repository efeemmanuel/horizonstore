from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm, TextInput, EmailInput, PasswordInput


# from .models import ShippingDetails
from .models import ShippingDetails

class Signupform(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 300px;','placeholder': 'firstname'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 300px;','placeholder': 'lastname'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'max-width: 300px;','placeholder': 'Create a password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','style': 'max-width: 300px;','placeholder': 'Enter password again'}))
    #email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Username'
            }),
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email address'
            }),

        }




#coupon form
class CouponForm(forms.Form):
    code = forms.CharField(label='Coupon code')








class ShippingDetailsForm(forms.ModelForm):
    class Meta:
        model = ShippingDetails
        fields = ['firstname','lastname','address', 'city', 'state', 'country','zip_code','phone_number']























# PAYMENT_METHOD_CHOICES = [
#     ('paypal', 'PayPal'),
#     ('credit_card', 'Credit Card'),
#     ('bank_transfer', 'Bank Transfer'),
#     # Add more payment methods as needed
# ]
# COUNTRY = [
#     ('Nigeria', 'Nigeria'),
# ]
# STATE = [
#     ('Lagos', 'Lagos'),
#     ('Abia', 'Abia'),
#     ('Kano', 'Kano'),
#     ('kaduna', 'Kaduna'),
#     ('Abuja', 'Abuja'),
#     ('Kastina', 'Kastina'),
# ]
# CITY = [
#     ('option1', 'Option 1'),
#     ('option2', 'Option 2'),
#     ('option3', 'Option 3'),
# ]
# class ShippingDetailsForm(forms.ModelForm):

#     firstname = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 300px;'}))
#     lastname = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 300px;'}))
#     address = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 300px;'}))
#     zip_code = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 300px;'}))
#     phone_number = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 300px;'}))
#     payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES)
#     country = forms.ChoiceField(choices=COUNTRY, required=True,) 
#     city = forms.ChoiceField(choices=CITY, required=True,)
#     state = forms.ChoiceField(choices=STATE, required=True,)
    
    
#     class Meta:
#         model = ShippingDetails  # Specify the model class here
#         fields = ['address', 'state', 'city']
    












# COUNTRY = [
#     ('Nigeria', 'Nigeria'),
# ]
# STATE = [
#     ('Lagos', 'Lagos'),
#     ('Abia', 'Abia'),
#     ('Kano', 'Kano'),
#     ('kaduna', 'Kaduna'),
#     ('Abuja', 'Abuja'),
#     ('Kastina', 'Kastina'),
# ]
# CITY = [
#     ('option1', 'Option 1'),
#     ('option2', 'Option 2'),
#     ('option3', 'Option 3'),
# ]
# PAYMENT = [
#     ('Bank transfer', 'Bank transfer'),
#     ('pay with paypal', 'pay with paypal'),
#     ('option3', 'Option 3'),
# ]

# class ShippingAddressForm(forms.Form):
#     first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 300px;'}))
#     last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 300px;'}))
#     country = forms.ChoiceField(choices=COUNTRY, required=True,) 
#     address = forms.CharField(max_length=40, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 300px;'}))
#     city = forms.ChoiceField(choices=CITY, required=True,)
#     state = forms.ChoiceField(choices=STATE, required=True,)
#     zip_code = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 300px;'}))
#     phone_number = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control','style': 'max-width: 300px;'}))
#     email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control','style': 'max-width: 300px;'}))
#     payment_method = forms.ChoiceField(choices=PAYMENT, required=True,)
#     # Add more form fields as required for the shipping address

        




