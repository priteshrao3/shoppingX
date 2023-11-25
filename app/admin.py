from django.contrib import admin
from .models import MainSlider, Customer, Product, Cart, OrderPlaced

# Register your models here.
@admin.register(MainSlider)
class MainSliderAdmin(admin.ModelAdmin):
    list_display = ['image',]



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'brand', 'category', 'product_image']


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']



@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['id',]
