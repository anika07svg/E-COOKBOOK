from django.shortcuts import render, redirect, get_object_or_404
from .models import Merchant
from .forms import MerchantForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def showMerchants(request):
    merchantList = Merchant.objects.all()
    context = {
        'Merchant': merchantList
    }
    return render(request, 'MerchantManagement/MerchantList.html', context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()


    context = {
        'form' : form

    }
    return render(request, 'MerchantManagement/registration.html', context)

@login_required
def createProfile(request):

    merchant_list=Merchant.objects.filter(user=request.user)

    if len(merchant_list) != 0:
        merchant = Merchant.objects.get(user=request.user)
        form = MerchantForm(initial={'Merchant_Name': merchant.Merchant_Name,
                                     'M_Food_Name': merchant.M_Food_Name,
                                     'Business_Name': merchant.Business_Name,
                                     'Email': merchant.Email,
                                     'NID': merchant.NID,
                                     'Phone_Number': merchant.Phone_Number,
                                     'Address': merchant.Address,
                                     'Profile_pic': merchant.Profile_pic,
                                     })
    else:
        merchant = None
        form = MerchantForm()

    if request.method == "POST":
        form = MerchantForm(request.POST, request.FILES)

        if form.is_valid():
            if merchant == None:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()

            else:
                '''
                merchant.delete()

                merchant = Merchant(form.cleaned_data['Merchant_Name'],
                                    form.cleaned_data['M_Food_Name'],
                                    form.cleaned_data['Business_Name'],
                                    form.cleaned_data['Email'],
                                    form.cleaned_data['NID'],
                                    form.cleaned_data['Phone_Number'],
                                    form.cleaned_data['Address'],
                                    form.cleaned_data['Profile_pic'],
                                    request.user)

                '''



                merchant.Merchant_Name = form.cleaned_data['Merchant_Name']
                merchant.M_Food_Name = form.cleaned_data['M_Food_Name']
                merchant.Business_Name = form.cleaned_data['Business_Name']
                merchant.Email = form.cleaned_data['Email']
                merchant.NID = form.cleaned_data['NID']
                merchant.Phone_Number = form.cleaned_data['Phone_Number']
                merchant.Address = form.cleaned_data['Address']
                merchant.Profile_pic = form.cleaned_data['Profile_pic']

                merchant.save()

            return redirect('Merchant')
    context = {

        'form': form
    }
    return render(request, 'MerchantManagement/editMerchant_Profile.html', context)

@login_required
def show_Merchant_Profile(request):
    global merchant
    try:
        merchant = Merchant.objects.get(user=request.user)
    except Merchant.DoesNotExist:
        merchant = "Please complete your profile to view"

    context = {
        'Merchant': merchant
    }

    return render(request, 'MerchantManagement/showMerchantProfile.html', context)





