from django.contrib import admin
from .models import Order,OrderProduct,Payment

# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user','payment_id','payment_method','amount_paid','status','created_at')
admin.site.register(Payment,PaymentAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','payment','order_number','phone','email','address_line1','address_line2','country','state','city','order_total','tax','status','ip','is_ordered','created_at','updated_at')
admin.site.register(Order,OrderAdmin)

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('user','order','payment','product','variation','color','size','quantity','product_price','ordered','created_at','updated_at')
admin.site.register(OrderProduct,OrderProductAdmin)
