from django.contrib import admin
from . models import Customer, Product, Cart, Cartitems, ShippingAddress
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(ShippingAddress)

