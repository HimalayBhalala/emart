from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length = 30,unique = True)
    slug = models.SlugField(max_length = 30)
    description = models.TextField(max_length = 500,blank=True)
    image_upload = models.ImageField(upload_to='image/categories',blank=False)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name