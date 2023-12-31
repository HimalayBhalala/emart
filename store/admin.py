from django.contrib import admin
from .models import Product,Variation,ReviewRating,ProductGallary
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ProductGallaryInline(admin.TabularInline):
    model = ProductGallary
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','created_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}
    inlines = [ProductGallaryInline]

admin.site.register(Product,ProductAdmin)

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value','is_active')
    list_editable = ('is_active',)
    list_filter = ('product','variation_category','variation_value')
admin.site.register(Variation,VariationAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','product','subject','rating','review','status','created_at','updated_at')
admin.site.register(ReviewRating,ReviewAdmin)


admin.site.register(ProductGallary)