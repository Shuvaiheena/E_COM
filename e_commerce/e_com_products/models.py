from django.db import models
from e_com_customer.models import CustomerDetails
# Create your models here.
class ProductDetails(models.Model):
    prod_id = models.BigAutoField(primary_key=True)
    prod_name = models.CharField(max_length=100, blank=True, null=True)
    prod_code = models.CharField(max_length=25, blank=True, null=True)
    prod_date = models.DateField(blank=True, null=True)
    prod_age = models.BigIntegerField(blank=True, null=True)
    prod_active = models.IntegerField(blank=True, null=True,default=0) # 1. active products 2.inactive products
    customer= models.ForeignKey(CustomerDetails, models.DO_NOTHING, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'product_details'

    def __str__(self):
        return str(self.prod_name)