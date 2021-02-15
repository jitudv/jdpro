from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50,null=True)
    product_price= models.IntegerField(null=False)
    product_manufacturer = models.CharField(max_length=50)
    product_mfg_date = models.DateField()



