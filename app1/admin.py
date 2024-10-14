# admin.py
from django.contrib import admin
from .models import UserDetails, Product, Order, Category

# admin.py
from django.contrib import admin
from .models import UserDetails, Product, Order, Category

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_customer', 'is_staff','profile_picture')
    search_fields = ('username', 'email')
    list_filter = ('is_customer', 'is_staff')

    def save_model(self, request, obj, form, change):
        if form.cleaned_data['password']:
            obj.set_password(form.cleaned_data['password'])  # Hash the password
        super().save_model(request, obj, form, change)

admin.site.register(UserDetails, UserDetailsAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category',)


# admin.py
from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'quantity', 'status')
    search_fields = ('product', 'user')
    list_filter = ('status',)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)