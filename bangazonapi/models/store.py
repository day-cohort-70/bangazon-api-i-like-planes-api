from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from .customer import Customer
from django.contrib.auth.models import User
from .productcategory import ProductCategory
from .orderproduct import OrderProduct
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE
from .product import Product

class Store(models.Model):

    seller = models.OneToOneField(Customer, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100,)
    description = models.CharField(max_length=255,)

    @property
    def product_count(self):
        """product_count property of a store

        Returns:
            int -- Number products with store_id
        """
        products = Product.objects.filter(store = self)
        return products.count()

