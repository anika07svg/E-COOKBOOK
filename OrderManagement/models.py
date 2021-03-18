from django.db import models
from FoodManagement.models import Food
from MerchantManagement.models import Merchant
from CustomerManagement.models import Customer
from django.contrib.auth.models import User



# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Delivering', 'Delivering'),
        ('Completed', 'Completed')
    )

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')

    PAYMENT_CHOICES = (
        ('Bkash', 'Bkash'),
        ('Rocket', 'Rocket'),
        ('Payment on delivery', 'Payment on delivery')
    )
    payment_options = models.CharField(max_length=50, choices=PAYMENT_CHOICES, default='Payment on delivery')
    is_paid = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=30, null=True, blank=True)

    food = models.ForeignKey(Food, on_delete=models.CASCADE, default=1)
    #merchant = models.ForeignKey(Merchant, on_delete=models.SET_NULL, null=True)
    #customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username + "-" + self.food.Food_Name + "-" + self.status

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     food = models.ManyToManyField(Food) # can be blank or null by default
#     created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#     def __str__(self):
#         return self.user.username