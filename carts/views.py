from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from store.models import Product
from .models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist
from store.models import Variation

# Create your views here.

def _card_id(request):
    cart = request.session.session_key

    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    product_variation = []
    if request.method == "POST":
        for item in request.POST:
            key = item
            value = request.POST[key]
            try:
                variation = Variation.object.get(product=product,variation_category__iexact=key,variation_value__iexact=value)
                product_variation.append(variation)
            except:
                pass
    try:
        cart = Cart.objects.get(cart_id = _card_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _card_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        if len(product_variation) > 0:
            cart_item.variations.clear()
            for item in product_variation:
                cart_item.variations.add(item)
        print(cart_item.variations)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        if len(product_variation) > 0:
            cart_item.variations.clear()
            for item in product_variation:
                cart_item.variations.add(item)
        cart_item.save()
    return redirect('cart')

def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id = _card_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(product=product,cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id = _card_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.filter(product=product,cart=cart)

    cart_item.delete()

    return redirect('cart')


def cart(request,total=0,quantity=0,context=None):
    try:
        cart = Cart.objects.get(cart_id = _card_id(request))
        cart_items = CartItem.objects.filter(cart=cart,is_active = False)

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2*total)/100
        grand_total = total + tax
        print(total)
    except ObjectDoesNotExist:
        pass

    context = {
        'total':total,
        'quantity':quantity,
        'cart_items': cart_items,
        'tax' : tax,
        'grand_total' : grand_total,
    }
    print(cart_items)


    return render(request,'store/cart.html',context)


    
