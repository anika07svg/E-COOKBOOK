from django import forms
from .models import Food,Review


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('Food_Name','Food_Price','Food_Category','Food_Image')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')