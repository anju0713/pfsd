from .forms import UserEditForm, UserProfileForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import UserDetails, Category
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserDetails
from .forms import UserForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserDetails
from .forms import UserForm
from .forms import ProductForm
from django.contrib.auth.decorators import user_passes_test
from .models import UserDetails, Product

'''def index(request):
    return render(request, "app1/index.html")'''

# views.py
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserDetails, Product,  CartItem
from .forms import UserEditForm, UserForm, ProductForm

# views.py
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserDetails, Product,  CartItem
from .forms import UserEditForm, UserForm, ProductForm

def login_selection(request):
    return render(request, 'app1/login_selection.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_admin:
            auth_login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid admin credentials')
    return render(request, 'app1/admin_login.html')

@user_passes_test(lambda u: u.is_admin)
def admin_dashboard(request):
    customers = UserDetails.objects.filter(is_customer=True)
    products = Product.objects.all()
    orders = Order.objects.all()
    return render(request, 'app1/admin_dashboard.html', {
        'customers': customers,
        'products': products,
        'orders': orders,
    })

def admin_logout(request):
    auth_logout(request)
    return redirect('login_selection')

# views.py
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserDetails, Product,  CartItem
from .forms import UserEditForm, UserForm, ProductForm

# views.py
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserDetails

# views.py
from django.shortcuts import redirect
from django.urls import reverse

def customer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_customer:
            auth_login(request, user)
            return redirect(reverse('user_home', kwargs={'user_id': user.id}))
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'app1/customer_login.html')
# views.py
from django.shortcuts import render, get_object_or_404
from .models import  UserDetails


from .models import Order

@login_required
def user_home(request, user_id):
    user_details = get_object_or_404(UserDetails, id=user_id)
    products = Product.objects.all()
    orders = Order.objects.filter(user_id=user_id)  # Correct the query to use 'user_id'
    cart = CartItem.objects.filter(cart__user=user_details)  # Correct the query to use 'cart__user'
    return render(request, 'app1/user_home.html', {
        'user': user_details,
        'products': products,
        'cart': cart,
        'orders': orders
    })

def user_logout(request):
    auth_logout(request)
    return redirect('customer_login')




#for user:

def user_list(request):
    users = UserDetails.objects.all()
    return render(request, 'app1/user_list.html', {'users': users})
# firstproject/app1/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            messages.success(request, 'User added successfully.')
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'app1/add_user.html', {'form': form})
# firstproject/app1/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserEditForm
from .models import UserDetails

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserEditForm
from .models import UserDetails

def edit_user(request, id):
    user = get_object_or_404(UserDetails, id=id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=user)  # Include request.FILES to handle file uploads
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully.')
            return redirect('user_list')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'app1/edit_user.html', {'form': form})
def delete_user(request, id):
    user = get_object_or_404(UserDetails, id=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully.')
        return redirect('admin_dashboard')
    return render(request, 'app1/confirm_delete.html', {'user': user})

#for product:

def product_list(request):
    products = Product.objects.all()
    return render(request, 'app1/product_list.html', {'products': products})
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'app1/add_product.html', {'form': form})
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)  # Handle file uploads
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'app1/edit_product.html', {'form': form, 'product': product})
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        if product.image:
            product.image.delete()  # Delete the image file
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('product_list')
    return render(request, 'app1/delete_product.html', {'product': product})


#for order:

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'app1/order_list.html', {'orders': orders})

#for category:

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'app1/category_list.html', {'categories': categories})





# firstproject/app1/views.py
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserDetails
# app1/views.py
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .forms import PasswordResetForm
from .models import UserDetails

def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = UserDetails.objects.filter(email=email).first()
            if user:
                reset_link = request.build_absolute_uri(reverse('reset_password', args=[user.id]))
                send_mail(
                    'Password Reset Request',
                    f'Click the link to reset your password: {reset_link}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'A reset link has been sent to your email.')
            else:
                messages.error(request, 'No user found with this email.')
            return redirect('forgot_password')
    else:
        form = PasswordResetForm()
    return render(request, 'app1/forgot_password.html', {'form': form})
# app1/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import PResetForm

# app1/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import PasswordResetForm
from .models import UserDetails  # Import the custom user model

def reset_password(request, user_id):
    user = get_object_or_404(UserDetails, id=user_id)  # Use UserDetails instead of User
    if request.method == 'POST':
        form = PResetForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Your password has been reset successfully.')
            return redirect('login_selection')
    else:
        form = PResetForm()
    return render(request, 'app1/reset_password.html', {'form': form})
# firstproject/app1/views.py
from django.shortcuts import render, get_object_or_404
from .models import UserDetails

def user_detail(request, id):
    user = get_object_or_404(UserDetails, id=id)
    return render(request, 'app1/user_detail.html', {'user': user})
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
# firstproject/app1/views.py
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem

# firstproject/app1/views.py

# firstproject/app1/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserEditForm
from .models import UserDetails

# firstproject/app1/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserEditForm
from .models import UserDetails
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserEditForm
from .models import UserDetails
from django.contrib.auth.decorators import login_required
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserEditForm
from .models import UserDetails
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserEditForm
from .models import UserDetails
from django.contrib.auth.decorators import login_required
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserEditForm
from .models import UserDetails
from django.contrib.auth.decorators import login_required

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import UserEditForm
from .models import UserDetails
from django.contrib.auth.decorators import login_required

@login_required
def edit_profile(request, id):
    user_details = get_object_or_404(UserDetails, id=id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=user_details)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('user_home', user_id=user_details.id)  # Correct the keyword argument
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserEditForm(instance=user_details)
    return render(request, 'app1/edit_profile.html', {'form': form})


from django.contrib.auth.decorators import login_required
from .models import Product, CartItem
# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Product, CartItem, UserDetails
# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Product, CartItem, UserDetails


from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth.decorators import login_required


from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

def logout(request):
    """Logs out the user and redirects to the login page."""
    auth_logout(request)  # This logs out the user
    return redirect('login')  # Redirect to the login page after logout


from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404
from .models import UserDetails

def user_detail(request, id):
    user = get_object_or_404(UserDetails, id=id)
    return render(request, 'app1/user_detail.html', {'user': user})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserDetails
#from .forms import ProfilePictureForm

'''@login_required
def change_profile(request):
    user = get_object_or_404(UserDetails, username=request.user.username)
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user_id=user.id)
    else:
        form = ProfilePictureForm(instance=user)
    return render(request, 'app1/change.html', {'form': form})'''
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fullname = request.POST['fullname']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if UserDetails.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif UserDetails.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                hashed_password = make_password(password)  # Hashing the password here
                user = UserDetails(username=username, email=email, name=fullname, password=hashed_password)
                user.is_customer=True
                user.save()
                messages.success(request, 'User registered successfully')
                return redirect('customer_login')  # Redirect to customer_login after successful registration
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'app1/index.html')
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'app1/product_detail.html', {'product': product})
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, UserDetails

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem, UserDetails

def add_to_cart(request, user_id, product_id):
    user = get_object_or_404(UserDetails, id=user_id)  # Ensure this query is correct
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart', user_id=user_id)

# views.py
# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product

# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product

# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product
# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Cart, CartItem

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Cart, CartItem

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Cart, CartItem

from django.shortcuts import render, get_object_or_404
from .models import UserDetails, Cart, CartItem
from django.contrib.auth.decorators import login_required
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import CartItem
from django.contrib.auth.decorators import login_required

@login_required
def update_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()
    return redirect('cart', user_id=request.user.id)

@login_required
def buy_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    # Implement the logic for buying the item
    # For now, just redirect to the cart
    return redirect('cart', user_id=request.user.id)
@login_required
def cart(request, user_id):
    user = get_object_or_404(UserDetails, id=user_id)
    cart = get_object_or_404(Cart, user=user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'app1/cart.html', {'cart_items': cart_items})
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart', user_id=request.user.id)

def checklogin(request):
    """Handle manual user login using custom user model."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.GET.get('next', '')  # Get the next URL or default to user detail page

        try:
            user = UserDetails.objects.get(username=username)
            if check_password(password, user.password):
                auth_login(request, user)  # Log the user in manually
                # Redirect to the user detail page after login
                return redirect('user_detail', user_id=user.id)
            else:
                messages.error(request, 'Invalid username or password')
        except UserDetails.DoesNotExist:
            messages.error(request, 'Invalid username or password')

    next_url = request.GET.get('next', '')
    return render(request, 'app1/login.html', {'next': next_url})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderStatusForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

@login_required
def order_form(request, product_id,quantity):
    product = get_object_or_404(Product, id=product_id)
    total_price=product.price*quantity
    user = request.user

    if request.method == 'POST':
        Order.objects.create(
                product=product,
                user=user,
                quantity=quantity,
                price=total_price,
                address=request.POST['address'],
                phone_number=request.POST['phone_number'],
                payment_type=request.POST['payment_type'],
                status='pending'
            )
        return redirect('user_home', user_id=user.id)
    return render(request, 'app1/order_form.html', {'product': product, 'quantity':quantity, 'total_price':total_price})
@login_required
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderStatusForm(instance=order)
    return render(request, 'app1/update_order_status.html', {'form': form, 'order': order})
@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    order = Order(product=product, user=user, quantity=1, price=product.price)
    order.save()
    return redirect('user_home', user_id=user.id)
# views.py
from django.shortcuts import render
from .models import Order

def track_order(request, user_id):
    orders = Order.objects.filter(user_id=user_id)
    return render(request, 'app1/track_order.html', {'orders': orders})
    return render(request, 'app1/track_order.html', {'orders': orders})