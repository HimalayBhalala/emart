from django.shortcuts import render,redirect
from django.http import HttpResponse
from carts.models import CartItem
from .forms import OrderForm
from .models import Order
import datetime

# Create your views here.

def place_order(request,total=0,quantity=0):
    current_user = request.user

    #if cart_count is less than or equal to 0 then redirect back to shop
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count  = cart_items.count()
    if cart_count <= 0:
        return redirect('store')
    
    tax = 0
    grand_total = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        quantity += cart_item.quantity
    tax = (2*total)/100
    grand_total = total + tax

    
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            #store all the biling information inside order table
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line1 = form.cleaned_data['address_line1']
            data.address_line2 = form.cleaned_data['address_line2']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.tax = tax
            data.order_total = grand_total
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            #generate ordernumber 
            yr = int(datetime.date.today().strftime('%Y'))
            mt = int(datetime.date.today().strftime('%m'))
            dt = int(datetime.date.today().strftime('%d'))
            d = datetime.date(yr,mt,dt)
            current_date = d.strftime("%Y%m%d")#20211226
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()
            return redirect('checkout')
    else:
        return redirect('checkout')    
