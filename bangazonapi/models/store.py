from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from .customer import Customer
from .productcategory import ProductCategory
from .orderproduct import OrderProduct
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE

class Store(models.Model):

    seller = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name='store_seller')
    name = models.CharField(max_length=100,)
    description = models.CharField(max_length=255,)