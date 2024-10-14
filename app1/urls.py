# urls.py
from django.urls import path
from app1 import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', views.register, name='register'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_to_cart/<int:user_id>/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/<int:user_id>/', views.cart, name='cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<int:cart_item_id>/', views.update_quantity, name='update_quantity'),
    path('buy_item/<int:cart_item_id>/', views.buy_item, name='buy_item'),
    path('user_home/<int:user_id>/', views.user_home, name='user_home'),
    path('place_order/<int:product_id>/', views.place_order, name='place_order'),
    path('order_form/<int:product_id>/<int:quantity>/', views.order_form, name='order_form'),
    path('track_order/<int:user_id>/', views.track_order, name='track_order'),
    path('update_order_status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('user/<int:id>/', views.user_detail, name='user_detail'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('reset_password/<int:user_id>/', views.reset_password, name='reset_password'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('edit_profile/<id>', views.edit_profile, name='edit_profile'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('add_user/', views.add_user, name='add_user'),
    path('users/', views.user_list, name='user_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/', views.product_list, name='product_list'),
    path('orders/', views.order_list, name='order_list'),
    path('categories/', views.category_list, name='category_list'),
    path('add_user/', views.add_user, name='add_user'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('edit_user/<int:id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    path('', views.customer_login, name='login_selection'),  # Redirect to customer login
    path('customer_login/', views.customer_login, name='customer_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)