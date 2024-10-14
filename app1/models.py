

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AdminManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('The Username field is required')
        user = self.model(username=username)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Admin(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AdminManager()

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'admin'

    def __str__(self):
        return self.username



class Category(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=100, default='default_category')
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    class Meta:
        db_table = 'product'

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.conf import settings

# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserDetailsManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class UserDetails(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='images/', default='images/default.jpg')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserDetailsManager()

    class Meta:
        db_table = 'userdetails'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
# models.py
from django.db import models
from django.conf import settings

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=1)  # Provide a default value
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

from django.db import models
from django.conf import settings
from django.utils import timezone
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Acceptance Pending'),
        ('accepted', 'Accepted the Order'),
        ('sent', 'Sent to Delivery'),
        ('delivered', 'Delivered'),
    ]

    PAYMENT_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cash_on_delivery', 'Cash on Delivery'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15,default='000-000-0000')
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='credit_card')
    created_at = models.DateTimeField(default=timezone.now)

    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_user(user_id):
        return Order.objects.filter(user_id=user_id)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.product.name
