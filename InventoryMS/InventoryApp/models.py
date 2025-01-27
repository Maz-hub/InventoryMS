from django.db import models

# Create your models here.

# Product table
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    product_sku = models.CharField(max_length=50, unique=True)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    product_weight = models.FloatField()
    product_color = models.CharField(max_length=100)
    product_size = models.CharField(max_length=50)
    product_supplier = models.CharField(max_length=300)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.product_name
