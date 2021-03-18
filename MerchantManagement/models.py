from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Merchant(models.Model):
    Merchant_Name = models.CharField(max_length=100)
    M_Food_Name = models.CharField(max_length=200)
    Business_Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    NID = models.CharField(max_length=200)
    Phone_Number = models.IntegerField()
    Address = models.CharField(max_length=200)
    Profile_pic = models.ImageField(upload_to='images/Profile_pic/',default='default.jpg')


    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)


    def __str__(self):
        return self.Merchant_Name


