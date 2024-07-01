from django.db import models


class OrderProduct(models.Model):

    order = models.ForeignKey("Order",
                              on_delete=models.CASCADE,
                              related_name="lineitems")

    product = models.ForeignKey("Product",
                                on_delete=models.CASCADE,
                                related_name="lineitems")
