from django import forms
from .models import UserDetails

class UserForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['name', 'username', 'email', 'password', 'profile_picture']
        widgets = {
            'password': forms.PasswordInput(),
        }
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['name', 'username', 'email', 'profile_picture']
# forms.py
from django import forms
from .models import UserDetails

class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['name', 'username', 'email', 'profile_picture']
from django import forms
from .models import Product
# forms.py
from django import forms
from .models import UserDetails

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserDetails
        fields = ['username', 'email', 'password', 'name', 'profile_picture']
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category', 'image']  # Include image field
from django import forms
from .models import Order

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
from django import forms

class OrderForm(forms.Form):
    address = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=15)
    PAYMENT_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cash_on_delivery', 'Cash on Delivery'),
    ]
    payment_type = forms.ChoiceField(choices=PAYMENT_CHOICES)
class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Email",max_length=254)


# app1/forms.py
from django import forms


class PResetForm(forms.Form):
    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data