from django import forms
from .models import Merchant


class MerchantForm(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = ('Merchant_Name','M_Food_Name','Business_Name','Email','NID','Phone_Number','Address','Profile_pic')
