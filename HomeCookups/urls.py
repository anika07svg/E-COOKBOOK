"""HomeCookups URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from MerchantManagement import views as merchant_views
from CustomerManagement import views as customer_views
from FoodManagement import views as food_views
from OrderManagement import views as order_views
from BillManagement import views as bill_views

from django.conf import settings
from django.conf.urls.static import static

assert isinstance(settings.MEDIA_ROOT, object)
urlpatterns = [
    path('admin/', admin.site.urls),

    path('Merchant/', merchant_views.showMerchants, name='Merchant'),
    path('viewMProfile/', merchant_views.show_Merchant_Profile, name='View_Profile'),
    path('CompleteProfile/', merchant_views.createProfile, name='Complete_Profile'),

    path('Customer/',customer_views.showCustomers, name = 'Customer' ),
    path('c_viewCProfile/', customer_views.show_Customer_Profile, name='C_View_Profile'),
    path('c_CompleteProfile/', customer_views.createProfile, name='C_Complete_Profile'),

    path('Food/', food_views.showFoods, name='Food'),
    path('insertFood/', food_views.insertFood, name='insertFood'),
    path('Food/<int:Food_id>', food_views.showDetails, name='Food_Details'),
    path('bkash/<int:food_id>', food_views.bkash_order, name='bkash-order-food'),
    path('review/<int:Food_id>', food_views.review_after_complete, name='review'),

    path('Order/', order_views.showOrders, name='Order'),
    path('myOrder/', order_views.my_orders, name='my_order'),
    path('orderFood/<int:food_id>', order_views.make_order, name='order-food'),


    path('Bill/', bill_views.showBills, name='Bill'),
    path('insertBill/', bill_views.insertBill, name='insertBill'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('merchantregistration/', merchant_views.registration, name='merchant_registration'),
    path('customerregistration/', customer_views.registration, name='customer_registration'),

    path('', food_views.main_home, name='main-home'),
    path('cart/', food_views.view_cart, name='cart'),
    path('updatecart/<int:food_id>', food_views.update_cart, name='update-cart'),
    path('deletefromcart/<int:food_id>', food_views.delete_from_cart, name='delete-from-cart')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
'''


