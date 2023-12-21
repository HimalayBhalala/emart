from django.db import models
from mart.models import Category

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    images = models.ImageField(upload_to='image/product')
    stock = models.IntegerField()
    is_available = models.BooleanField(default = True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name