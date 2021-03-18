from django.contrib import admin
from .models import Food,Cart,Review

# Register your models here.
admin.site.register([Food,Cart,Review])
