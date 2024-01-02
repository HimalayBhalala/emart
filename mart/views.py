from django.shortcuts import render,get_object_or_404
from store.models import Product,ReviewRating
from .models import Category

# Create your views here.

def home(request):

    products = Product.objects.all().filter(is_available = True).order_by('created_date')

    for product in products:
        reviews = ReviewRating.objects.filter(product_id = product.id,status=True)

    context = {
        'products':products,
        'reviews':reviews,
    }
    return render(request,'mart/home.html',context)


