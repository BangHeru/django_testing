from django.contrib import admin


# register Product model from ./models

from .models import Product

admin.site.register(Product)
