from django.shortcuts import render,get_object_or_404
from store.models import Product
from .models import Category

# Create your views here.

def home(request):
    products = Product.objects.all().filter(is_available = True)

    context = {
        'products':products,
    }
    return render(request,'mart/home.html',context)


