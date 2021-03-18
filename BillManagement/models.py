from django.db import models
from OrderManagement.models import Order
from CustomerManagement.models import Customer


class Bill(models.Model):
    Payment_Type = models.CharField(max_length=100)
    Total_Price = models.FloatField(max_length=200)

    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    @property
    def __str__(self):
        return self.Payment_Type
