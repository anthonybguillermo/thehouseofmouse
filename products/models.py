from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    # image1 = models.ImageField() have installed Pillow, buy need to work out storage see https://docs.djangoproject.com/en/2.2/ref/models/fields/#imagefield
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    num_in_stock = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    num_sold = models.PositiveSmallIntegerField(default=0)
    gift_wrap = models.BooleanField(default=True)