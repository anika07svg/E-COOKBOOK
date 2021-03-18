from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    Phone_Number = models.IntegerField()
    Address = models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to='images/C_Profile_pic/',default='default.jpg')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.customer_name
