from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Product(models.Model):
    # category = models.ForeignKey(Category) - create table for this in shipping app
    shipping_profile = models.ForeignKey(
        'shipping.Shipping_profile',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    # image1 = models.ImageField() have installed Pillow, but need to work out storage see https://docs.djangoproject.com/en/2.2/ref/models/fields/#imagefield
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    gift_wrap = models.BooleanField(default=True)
    
    tags = models.CharField(max_length=300)
    num_in_stock = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    num_sold = models.PositiveSmallIntegerField(default=0)
    num_fav = models.PositiveSmallIntegerField(default=0)

class Category(models.Model):
    category_name = models.CharField(max_length=50)