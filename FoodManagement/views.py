from django.shortcuts import render,get_object_or_404, redirect, HttpResponseRedirect
from .models import Food,Cart
from .models import Review
from .forms import FoodForm,ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from OrderManagement.models import Order
from django.urls import reverse

# Create your views here.
def showFoods(request):
    foodList = Food.objects.all()

    if request.method == 'POST':
        foodList  = Food.objects.filter(Food_Name__icontains = request.POST['search'])
        #Food_Desc = Food.objects.filter(description__icontains = request.POST['search'])
        Food_Category = Food.objects.filter(Food_Category__icontains=request.POST['search'])

        #foodList = Food_Name | Food_Category | Food_Desc # C = A U B set operation

        foodList = foodList | Food_Category

    context = {
        'Food': foodList
    }
    return render(request, 'FoodManagement/FoodList.html', context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }
    return render(request, 'FoodManagement/registration.html', context)

@login_required
def insertFood(request):
    message = ""
    form = FoodForm()

    if request.method == "POST":
        form = FoodForm(request.POST,request.FILES)
        message = "Invalid input. Please try again!"
        if form.is_valid():
            form.save()
            return redirect('insertFood')
            message = "Food is inserted to DB. You can insert a new food now"
            form = FoodForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'FoodManagement/insertFood.html', context)


def main_home(request):
    return render(request, 'main_home.html')

def showDetails(request, Food_id):
    searched_food = get_object_or_404(Food, id=Food_id)

    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            searched_food.reviews.add(instance)
            searched_food.save()

    context = {
        'search': searched_food,
        'form': form
    }
    return render(request, 'FoodManagement/detail_product_view.html', context)


@login_required
def view_cart(request):

    #cart = Cart.objects.get(user=request.user)

    cart_list = Cart.objects.filter(user=request.user)
    if len(cart_list) == 0:
        # create a new cart for new user
        cart = Cart(user=request.user)
        cart.save()
    else:
        cart = cart_list[0]


    total = 0
    for food in cart.food.all():
        total += food.Food_Price

    context = {
        'cart': cart,
        'total' : total
    }

    return render(request, 'FoodManagement/cart.html', context)

def bkash_order(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    order = Order(user=request.user, food=food)
    order.transaction_id = request.POST['transaction_id']
    order.payment_options  = 'Bkash'
    order.save()

    cart = Cart.objects.get(user=request.user)
    cart.food.remove(food)
    cart.save()

    #return HttpResponseRedirect(reverse('cart'))
    return redirect('cart')

@login_required
def update_cart(request, food_id):

    food = get_object_or_404(Food, id=food_id)

    cart_list = Cart.objects.filter(user = request.user)
    if len(cart_list) == 0:
        # create a new cart for new user
        cart = Cart(user=request.user)
        cart.save()
    else:
        cart = cart_list[0]

    #cart = get_object_or_404(Cart, user=request.user)

    cart.food.add(food)
    cart.save()

    return redirect('cart')

'''
try:
    cart = Cart.objects.get(user=request.user)

except cart.DoesNotExist:
    cart = Cart(user=request.user)
'''

@login_required
def delete_from_cart(request, food_id):

    food = get_object_or_404(Food, id=food_id)
    cart = Cart.objects.get(user=request.user)

    cart.food.remove(food)
    cart.save()

    return redirect('cart')

@login_required
def review_after_complete(request, food_id):

    already_reviewed = False

    searched_food = get_object_or_404(Food, id=food_id)

    user_list = searched_food.reviews.filter(user=request.user)
    print(user_list, len(user_list))
    if len(user_list) != 0:
        already_reviewed = True


    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            searched_food.reviews.add(instance)
            searched_food.save()

            return redirect('my-orders')

    context = {
        'search': searched_food,
        'form': form,
        'already_reviewed': already_reviewed
    }
    return render(request, 'FoodManagement/detail_product_view_review.html', context)