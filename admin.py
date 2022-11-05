from django.contrib import admin
from shop.models import Product
from shop.models import Contact
from shop.models import Orders
from shop.models import OrderUpdate

# from shop.models import Category


# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)


# admin.site.register(Category)