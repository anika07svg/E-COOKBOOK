from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def showCustomers(request):
    customerList = Customer.objects.all()
    context = {
        'Customer': customerList
    }

    print(customerList)

    return render(request, 'CustomerManagement/CustomerList.html', context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }
    return render(request, 'CustomerManagement/registration.html', context)

@login_required
def show_Customer_Profile(request):

    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        customer = "Please complete your profile to view"

    context = {
        'Customer': customer
    }

    return render(request, 'CustomerManagement/showCustomerProfile.html', context)

@login_required
def createProfile(request):

    customer_list=Customer.objects.filter(user=request.user)

    if len(customer_list) != 0:
       customer = Customer.objects.get(user=request.user)
       form = CustomerForm(initial={'customer_name': customer.customer_name,
                                     'Phone_Number': customer.Phone_Number,
                                     'Address': customer.Address,
                                     'profile_pic': customer.profile_pic,
                                     })
    else:
        customer = None
        form = CustomerForm()

    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)

        if form.is_valid():
            if customer == None:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()

            else:
                '''
                customer.delete()

                customer = Customer(form.cleaned_data['customer_name'],
                                    form.cleaned_data['Phone_Number'],
                                    form.cleaned_data['Address'],
                                    form.cleaned_data['profile_pic'],
                                    request.user)

                '''



                customer.customer_name = form.cleaned_data['customer_name']
                customer.Phone_Number = form.cleaned_data['Phone_Number']
                customer.Address = form.cleaned_data['Address']
                customer.profile_pic = form.cleaned_data['profile_pic']

                customer.save()

            return redirect('Customer')
    context = {

        'form': form
    }
    return render(request, 'CustomerManagement/editCustomer_Profile.html', context)


