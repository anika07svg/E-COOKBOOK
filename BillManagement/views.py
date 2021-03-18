from django.shortcuts import render
from .models import Bill
from .forms import BillForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def showBills(request):
    billList = Bill.objects.all()
    context = {
        'Bill': billList
    }
    return render(request,'BillManagement/BillList.html', context)

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
def insertBill(request):
    message = ""
    form = BillForm()

    if request.method == "POST":
        form = BillForm(request.POST,)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            message = "Bill is inserted to DB. You can insert a new bill now"
            form = BillForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'BillManagement/insertBill.html', context)