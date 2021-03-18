from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Food
from django.urls import reverse
from FoodManagement .models import Cart

# Create your views here.
def showOrders(request):
    orderList = Order.objects.all()
    context = {
        'Order': orderList
    }
    return render(request, 'OrderManagement/OrderList.html', context)


def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }
    return render(request, 'OrderManagement/registration.html', context)

@login_required
def my_orders(request):
    orders = Order(user=request.user)

    try:
        orders = Order.objects.filter(user=request.user)
        order_status = True
    except orders.DoesNotExist:
        orders = Order(user=request.user)
        order_status = False

    total = 0.0
    for order in orders:
        total += order.food.Food_Price


    context = {
        'orders': orders,
        'order_status': order_status,
        'total' : total

    }
    return render(request, 'OrderManagement/Order.html', context)


@login_required
def make_order(request, food_id):
    
    food = get_object_or_404(Food, id=food_id)
    order = Order(user=request.user, food=food)
    order.save()
    print("Order done!")

    cart = Cart.objects.get(user=request.user)
    cart.food.remove(food)
    cart.save()
    print("Remove done!")

    return redirect('cart')

def test(request):

    print(request.POST)

    return redirect('Food')





# def bkash_order(request, food_id):
#     food = get_object_or_404(Food, id=food_id)
#     order = Order(user=request.user, food=food)
#     order.transaction_id = request.POST['transaction_id']
#     order.payment_options  = 'Bkash'
#     order.save()
#
#     cart = Cart.objects.get(user=request.user)
#     cart.food.remove(food)
#     cart.save()
#
#     #return HttpResponseRedirect(reverse('cart'))
#     return redirect('cart')




#
# @login_required
# def update_cart(request, Food_id):
#
#     food = get_object_or_404(Food, id=Food_id)
#     cart = get_object_or_404(Cart, user=request.user)
#
#     cart.food.add(food)
#     cart.save()
#
#     return redirect('cart')
#
# '''
# try:
#     cart = Cart.objects.get(user=request.user)
# except cart.DoesNotExist:
#     cart = Cart(user=request.user)
# '''

# @login_required
# def delete_from_cart(request, Food_id):
#
#     food = get_object_or_404(Food, id=Food_id)
#     cart = Cart.objects.get(user=request.user)
#
#     cart.food.remove(food)
#     cart.save()
#
#     return redirect('cart')


@login_required
def make_order(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    order = Order(user=request.user, food=food)
    order.save()

    return redirect('Food')